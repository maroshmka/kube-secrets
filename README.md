# kube-secrets

Small package for easier management of kube secrets.

# usage

data json from stdin -> kube secret

```bash
$ vault read secret/my-app -format=json | jq '.data' | \ 
    kube-secrets create --name my-project-secrets -n my-namespace - 
```

data json from file -> kube secret
```bash
$ echo '{"a": "top-secret"}' > s.json
$ kube-secrets create --name my-project-secrets -n my-namespace --data-file=s.json
```

# what

__Problem:__ You want to export json/yaml file as kube secrets and use them.  Secrets need to be \
             encoded in base64. You need to write yaml manifest and put there encoded secrets.

This package should make it easier for you to just grab json and export it.
