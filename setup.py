from setuptools import setup, find_packages

setup(
    name="kube-secrets",
    version="0.0.1",
    description="Easier management of kubernetes secrets.",
    # long_description=get_long_description(),
    # long_description_content_type="text/markdown",
    author="hmka",
    author_email="hunka.mario@gmail.com",
    url="https://github.com/maroshmka/kube-secrets",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click", "kubernetes"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["kube-secrets=kube_secrets.cli:main"]},
    classifiers=[
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
