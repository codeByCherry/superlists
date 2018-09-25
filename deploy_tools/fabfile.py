from fabric.contrib.files import append
from fabric.contrib.files import exists
from fabric.contrib.files import sed
# 获取环境变量
from fabric.api import env
# 执行命令并获取命令行执行结果
from fabric.api import local
# 执行命令行
from fabric.api import run

import random
import os

# 添加实际项目中 github 中代码的位置
REPO_URL = 'git@github.com:codeByCherry/superlists.git'


def deploy():
    # host 是在命令行中指定具体的值
    # env.host 是通过命令行传入
    print(f'hostname:{env.host}')
    # env.user 是使用操作系统的用户名
    print(f'user:{env.user}')
    assert env.host is not None, 'use like fab deploy:host=www.somewhere.com'
    site_folder = f'/home/{env.user}/sites/{env.host}'
    source_folder = f'{site_folder}/source'

    _create_directory_structure_if_necessary(site_folder)

    _get_latest_source(source_folder)

    _update_settings(source_folder, env.host)

    _update_virtualenv(source_folder)

    _update_static_file(source_folder)

    _update_database(source_folder)


def _create_directory_structure_if_necessary(site_folder):
    for sub_folder in ('database', 'static', 'virtualenv', 'source'):
        run(f'mkdir -p {site_folder}/{sub_folder}')
        print("create sub folder success.....")


def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run(f'cd {source_folder} && git fetch')
    else:
        run(f'git clone {REPO_URL} {source_folder}')

    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'cd {source_folder} && git reset --hard {current_commit}')


def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/superlists/settings.py'
    assert exists(settings_path), '注意配置文件不存在！！！'

    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS = .+$',

        f'ALLOWED_HOSTS = [ '
        f'"{site_name}", '
        f']'
        )

    print("*"*30)
    print("env host:", env.host)
    print(f'add {site_name} to ALLOWED_HOSTS!')
    print("*"*30)

    secret_key_file = source_folder + '/superlists/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+><'
        # random.SystemRandom().choice(chars) 会在 chars 中 choice 一个随机字符
        # key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        key = ''.join(random.choice(chars) for _ in range(50))
        print("*"*30)
        print(f'key::{key}')
        print("*"*30)
        append(secret_key_file, f'SECRET_KEY="{key}"')

    assert exists(secret_key_file)
    # 删除已存在 SECRET_KEY
    sed(
        settings_path,
        'SECRET_KEY = .+',
        ''
    )
    key_line = '\nfrom .secret_key import SECRET_KEY'
    # append(settings_path, key_line)
    run(f'echo "{key_line}">>{settings_path}')


def _update_virtualenv(source_folder):
    virtualenv_folder = os.path.join(source_folder, '../virtualenv')
    if not exists(virtualenv_folder + '/bin/pip'):
        run(f'python3 -m venv {virtualenv_folder}')
    run(f'{virtualenv_folder}/bin/pip install -r {source_folder}/requirements.txt')


def _update_static_file(source_folder):
    run(
        f'cd {source_folder}'
        '&& ../virtualenv/bin/python3 manage.py collectstatic --noinput'
    )


def _update_database(source_folder):
    run(
        f'cd {source_folder}'
        f'&& ../virtualenv/bin/python3 manage.py migrate --noinput'
    )
