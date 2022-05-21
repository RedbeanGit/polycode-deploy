
# PolyCode Deploy

Provides some Python scripts and a docker-compose file to deploy, scale and update PolyCode services.

## Requirements

This project requires at least [Python 3.8](https://www.python.org/downloads/), [Pipenv](https://pypi.org/project/pipenv/) and [Docker Compose](https://docs.docker.com/compose/install/).

For Debian users, you can run the following commands to install Pipenv and Python 3.8 and Docker Compose:

```bash
$ apt install python3.8 pipenv docker-ce
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```

> For older Debian versions or Ubuntu based distributions, `docker-ce` exists under the name `docker.io` or `docker`.

> Scripts found in `scripts` folder are made to work on GNU/Linux distributions. **They may not work on other operating systems**.

## Installation

First clone this repo:

```bash
$ git clone git@github.com:RedbeanGit/polycode-deploy.git deploy
$ cd deploy
```

Install Python dependencies:

```bash
$ pipenv install
```

## Before running scripts

First navigate to the project root directory:

```bash
$ cd path/to/polycode/deploy
```

Enter the virtual environment created by Pipenv:

```
$ pipenv shell
```

You can now use scripts provided!

## Usage

First setup the environment variables and create required folders:

```bash
$ ./scripts/setup.py
```

Then start all the containers:

```bash
$ ./scripts/start.py
```

You can scale (down or up) a service:

```bash
$ ./scripts/scale.py SERVICE SCALE
```

You can also update a service while running. The old containers will be shut down and destroyed after restarting the new ones. Load balancing will automatically redirect request to new containers without interruption.

```bash
$ ./scripts/update.py [OPTIONS] SERVICE VERSION
```

Finally you can shutdown PolyCode containers:

```bash
$ ./scripts/stop.py
```

## Environment Variables

Local environment variables are stored in `.env` file.

### Backend related variables

**`COMPOSE_PROJECT_NAME`**

The name of the project. Default is `polycode`.

**`API_VERSION`**

The version of the API to deploy. Default is `1.0.0`.

**`NODE_ENV`**

The current environment for PolyCode API. Should be `DEVELOPMENT` or `PRODUCTION`. Default is `PRODUCTION`.

**`JWT_SECRET`**

A string used to generate tokens using JWT. Default is auto-generated.

**`DB_NAME_PRODUCTION`**

The name of the database to store data. Default is `polycodedb`.

**`DB_DIALECT`**

The dialect of the database to use. Default is `postgres`.

**`DB_HOST`**

The hostname or address of the database to connect. Default is `postgres`.

**`DB_PORT`**

The port to use to connect to the database. Default is `5432`.

**`DB_USER`**

The user of the database. Default is `polycodeapi`.

**`DB_PASS`**

The password used to authenticate to the database. Default is auto-generated.

**`VERIFICATION_CODE_EXPIRATION`**

The number of seconds a verification code is valid. Default is `600`.

**`BEARER`**

The name of the auth token header. Default is `Bearer`.

**`DOCKER_SOCKET_PATH`**

The path to the Docker socket. This is needed to allow the API to run code in new containers. Default is `/var/run/docker.sock`.

**`MAILER_HOST`**

The hostname or address of the mail server. **No default value**.

**`MAILER_PORT`**

The port of the mail server. Default is `587`.

**`MAILER_USER`**

The user of the mail server. Default is polycode API.

**`MAILER_PASS`**

The password of the mail server. Default is auto-generated.

**`APP_URL`**

The URL of the frontend. Default is `https://polycode.ml`.

### Frontend related variables

**`APP_VERSION`**

The version of the frontend to deploy. Default is `1.0.0`.

**`NEXT_PUBLIC_API_URL`**

The URL of the API. Default is `https://api.polycode.ml/api/v1`.