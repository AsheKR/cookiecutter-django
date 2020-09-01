import os
import secrets
import shutil
import string
import textwrap

# CHANGEME mark
CHANGEME = '__CHANGEME__'

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def _get_random_string(length=50):
    punctuation = string.punctuation.replace(
        '"', '',
    ).replace(
        "'", '',
    ).replace(
        '\\', '',
    ).replace(
        '$', '',  # see issue-271
    )

    chars = string.digits + string.ascii_letters + punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def _create_secret_key(config_path):
    # Generate a SECRET_KEY that matches the Django standard
    secret_key = _get_random_string()

    with open(config_path, 'r+') as config_file:
        # Replace CHANGEME with SECRET_KEY
        file_contents = config_file.read().replace(CHANGEME, secret_key, 1)

        # Write the results to the file:
        config_file.seek(0)
        config_file.write(file_contents)
        config_file.truncate()


def copy_local_configuration():
    """
    Handler to copy local configuration.
    It is copied from ``.template`` files to the actual files.
    """
    secret_template = os.path.join(
        PROJECT_DIRECTORY, 'sources', '.envs', '.env.template',
    )
    secret_config = os.path.join(
        PROJECT_DIRECTORY, 'sources', '.envs', '.env',
    )
    shutil.copyfile(secret_template, secret_config)
    _create_secret_key(secret_config)

    # Local config:
    local_template = os.path.join(
        PROJECT_DIRECTORY,
        'sources',
        'app',
        'config',
        'settings',
        'environments',
        'local.template.py',
    )
    local_config = os.path.join(
        PROJECT_DIRECTORY,
        'sources',
        'app',
        'config',
        'settings',
        'environments',
        'local.py',
    )
    shutil.copyfile(local_template, local_config)


copy_local_configuration()
