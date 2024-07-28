# Gemini CLI

A no frills CLI utility to access Google Gemini from command line or terminal. It is especially useful when there's a limitation to use a browser.


### Virtual env

If does not exist, create one:

```bash
$ python3 -m venv env
```

To activate:

```bash
$ source env/bin/activate
```

To deactivate:

```bash
$ deactivate
```

### Useful commands

Generate `requirement.txt` file:

```bash
$ pip3 freeze > requirements.txt
```

To install from the dependency file:

```bash
$ pip3 install -r requirements.txt
```

### Troubleshooting

As of 25th of July, the GRPC IO package has a bug that causes the problem to show error when interactive with it. [Turned out that's a bug in the latest version of library](https://github.com/google-gemini/generative-ai-python/issues/486#issuecomment-2248453986). To resolve had to downgrate the package: `pip install  grpcio==1.60.1`.