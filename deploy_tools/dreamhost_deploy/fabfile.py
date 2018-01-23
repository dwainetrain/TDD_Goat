from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

# Save this as template, and then make one that works on Dreamhost

# First attempt, it jumped into dwainebest.com and just installed away!
# The site doestn' work though...

REPO_URL = "https://github.com/dwainetrain/TDD_Goat.git"

# I've had to make my own adjustments to this file, as the folder names and structure
# are slightly different on the Dreamhost server
# static = public/static
# virtualenv = testGoat
# source = superlists
# if you see any errors, those differences are a good place to start...
# Hmmm...well if we're making this on a new site, maybe I could give them the
# appropriate name...``
# I'll need to setup fabric with the dreamhost instructions it appears...

def _create_directory_structure_if_necassary(site_folder):
    for subfolder in ('database', 'static', 'testGoat', 'superlists'):
        run(f'mkdir -p {site_folder}/{subfolder}')

def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run(f'cd {source_folder} && git fetch')
    else:
        run(f'git clone {REPO_URL} {source_folder}')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'cd {source_folder} && git reset --hard {current_commit}')

def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/superlists/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS = .+$',
        f'ALLOWED_HOSTS = ["{site_name}"]'
    )
    secret_key_file = source_folder + '/superlists/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(._=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, f'SECRET_KEY = "{key}"')
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')

def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../testGoat'
    if not exists(virtualenv_folder + '/bin/pip'):
        run(f'python3.6 -m venv {virtualenv_folder}')
    run(f'{virtualenv_folder}/bin/pip install -r {source_folder}/requirements.txt')

def _update_static_files(source_folder):
    run(
        f'cd {source_folder}'
        ' && ../testGoat/bin/python manage.py collectstatic --noinput'
    )

def _update_database(source_folder):
    run(
        f'cd {source_folder}'
        ' && ../testGoat/bin/python manage.py migrate --noinput'
    )


def deploy():
    site_folder = f'/home/{env.user}/{env.host}'
    source_folder = site_folder + '/superlists'
    _create_directory_structure_if_necassary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)