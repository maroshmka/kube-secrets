import base64
import json
from pprint import pprint

import click
import kubernetes


@click.group()
def main():
    pass


def load_json(s: str):
    data = None
    try:
        data = json.loads(s)
    except json.decoder.JSONDecodeError:
        click.secho("Invalid json...", fg="red")
        exit(1)
    except Exception as e:
        click.secho(e.args[0], fg="red")
        exit(1)
    return data


def create_secret(name, namespace, data):
    kubernetes.config.load_kube_config()

    from kubernetes import client
    v1 = client.CoreV1Api()
    secret = client.V1Secret(data=data, metadata=client.V1ObjectMeta(name=name))
    api_response = v1.create_namespaced_secret(namespace=namespace, body=secret)

    pprint(api_response)
    click.secho("Secret created.", fg="yellow")


@main.command(name="create")
@click.option("--name", type=str, required=True)
@click.option("--namespace", "-n", type=str, required=True)
@click.option("--data-file", type=click.Path(exists=True))
@click.argument("_input", type=click.File("rb"), required=False)
def create(name, namespace, _input, data_file):
    if _input and data_file:
        click.secho("You can pass only stdin or --data-file option.", fg="red")
        exit(1)

    if _input:
        raw_data = _input.read().decode()
    else:
        with open(data_file, "r") as f:
            raw_data = f.read()

    data = load_json(raw_data)

    click.secho("Encoding data", fg="yellow")
    encoded = {k: base64.b64encode(v.encode()).decode() for k, v in data.items()}
    click.secho("Encoded secrets to base64", fg="yellow")
    del data

    create_secret(name, namespace, encoded)


if __name__ == "__main__":
    main()
