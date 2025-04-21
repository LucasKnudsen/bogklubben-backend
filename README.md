# Bogklubben Backend

## Run API

```
uvicorn src.api.main:app --host 0.0.0.0 --port 8080 --reload
```

## Setup

To manually create a virtualenv on MacOS and Linux:

- Make sure Python 3.11 is installed

```
$ python3 --version
```

- Create a virtualenv

```
$ python3 -m venv .venv
```

- Activate the virtualenv

```
$ source .venv/bin/activate
```

```

If you are a Windows platform, you would activate the virtualenv like this:

```

% .venv\Scripts\activate.bat

```

Once the virtualenv is activated, you can install the required dependencies.

```

$ pip install -r requirements.txt

```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Local development
Initiate local resource:

```

docker-compose up

```

Run the API locally:

```

uvicorn src.api.main:app --host 0.0.0.0 --port 8080 --reload

```

## Useful commands

- `cdk ls` list all stacks in the app
- `cdk synth` emits the synthesized CloudFormation template
- `cdk deploy` deploy this stack to your default AWS account/region
- `cdk diff` compare deployed stack with current state
- `cdk docs` open CDK documentation
```
