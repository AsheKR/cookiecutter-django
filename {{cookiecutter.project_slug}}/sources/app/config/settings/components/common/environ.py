from environ import Env

from ..path import BASE_DIR

env = Env()
SOURCE_DIR = BASE_DIR.parent

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    env.read_env(str(SOURCE_DIR, ".envs", ".env"))
