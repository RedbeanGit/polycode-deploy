#!/usr/bin/env python3

import click
import dotenv
import os
import secrets


def get_random_secret_key():
    """
    Return a 50 character random string.
    """
    length = 50
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(secrets.choice(chars) for i in range(length))


@click.command()
def main():
    """Prepare the environment before starting Stowdo."""

    click.echo('Welcome to Stowdo Deploy setup.')
    click.echo('This script will let you define variables for your local environment.')
    click.echo('The proposals in brackets are the default values. Leave blank to use them.')

    secret_key = get_random_secret_key()
    database_key = get_random_secret_key()
    mailer_password = get_random_secret_key()

    envs = {
        'COMPOSE_PROJECT_NAME': 'polycode',
        'API_VERSION': click.prompt('API version', default='1.0.0'),
        'APP_VERSION': click.prompt('Frontend version', default='1.0.0'),
        'NODE_ENV': click.prompt('Environment', default='production'),
        'JWT_SECRET': click.prompt(
            'Jwt secret key [default is auto-generated]',
            default=secret_key,
            hide_input=True,
            show_default=False,
        ),
        'DB_NAME_PRODUCTION': click.prompt('Database name', default='polycodedb'),
        'DB_DIALECT': click.prompt('Database dialect', default='postgres'),
        'DB_HOST': click.prompt('Database host', default='postgres'),
        'DB_PORT': click.prompt('Database port', default=5432, type=click.types.INT),
        'DB_USER': click.prompt('Database user', default='polycodeapi'),
        'DB_PASS': click.prompt(
            'Database password [default is auto-generated]',
            default=database_key,
            hide_input=True,
            show_default=False,
        ),
        'VERIFICATION_CODE_EXPIRATION': click.prompt('Delay before verification code expiration (second)', default='600'),
        'BEARER': click.prompt('Bearer field name', default='Bearer'),
        'DOCKER_SOCKET_PATH': click.prompt('Path to docker socket', default='/var/run/docker.sock'),
        'MAILER_HOST': click.prompt('Mailer host'),
        'MAILER_PORT': click.prompt('Mailer port', default='587'),
        'MAILER_USER': click.prompt('Mailer user', default='polycodeapi'),
        'MAILER_PASS': click.prompt(
            'Mailer password [default is auto-generated]',
            default=mailer_password,
            hide_input=True,
            show_default=False,
        ),
        'APP_URL': click.prompt('Frontend URL', default='https://polycode.ml'),
        'NEXT_PUBLIC_API_URL': click.prompt('API URL', default='https://api.polycode.ml/api/v1'),
    }

    click.echo('Saving environment variables...')
    dotenv_file = dotenv.find_dotenv()

    if not dotenv_file:
        dotenv_file = '.env'

    dotenv.load_dotenv(dotenv_file)
    
    for key, value in envs.items():
        dotenv.set_key(dotenv_file, key, str(value), quote_mode='never')
    
    click.echo('Done')
    click.echo('Creating data folders...')

    for folder in ('db-data', 'letsencrypt', 'proxy-data'):
        try:
            os.mkdir(folder)
        except Exception:
            click.echo(f'Unable to create folder {folder}')

    click.echo('Done')


if __name__ == '__main__':
    main()
