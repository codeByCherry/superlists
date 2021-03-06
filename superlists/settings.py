"""
Django settings for superlists project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j_q&_xxno49609sg2%j9%$qah2bolnds$z+qwk$8_brq#ahs&@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TODO:: 由于 fab 的 sed 总是替换失败，导致 allowed_hosts 设置失败!故手动配置这个值
ALLOWED_HOSTS = ['localhost', 'www.oocoding.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'lists.apps.ListsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'superlists.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'superlists.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../database/db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../static'))

#  在服务器的终端输入下面指令
#   cd ~
#   # 使用 staging 表示这是一个过渡测试网站，不是正式上线的网站
#   export SITENAME=www.staging.oocoding.com
#   mkdir -p ~/sites/$SITENAME/database
#   mkdir -p ~/sites/$SITENAME/static
#   mkdir -p ~/sites/$SITENAME/virtualenv
#   手动部署代码到服务器
#   将服务器的公钥添加到 github 中
#   ssh-keygen -t rsa -C "somebody_qq@qq.com"
#   cat ~/.ssh/id_rsa.pub  内容设置到 github 中
#   git clone git://zhang....git ~/sites/$SITENAME/source
#   在终端配置服务器的 Python 环境。  python3 -m venv ../virtualenv
#   激活虚拟环境 source ../virtualenv/bin/active
#   安装 django
#   pip install djangto
#
#   安装 nginx
#   sudo apt install nginx
#   启动 nginx 检查 nginx 是否启动成功
#   sudo systemctl start nginx
#   访问 http://ip.address or http://web_name
#   检查是否看到nginx 的启动页面
#
#   检查 settings.py 是否关闭了调试模式 并绑定好可访问的域名
#   ALLOWED_HOSTS
#
#   配置 nginx 将80端口映射到服务器的 8000 端口
#   详情查看 nginx_setting.txt 文件
#   服务器端安装了 nginx 后可以通过 $nginx -t 测试配置文件是否正确。
#
#   以上只是简单完成 部署，但是在实际部署中不能使用 dgango 的内置服务器
#   并且不可以手动使用 ./manager runserver 实现服务器开启。
#   而是使用 nginx 提供静态文件服务， gunicorn 运行 django 代码！
#

#   使用 gunicorn 运行 django 代码
#   1: pip install gunicorn
#   2: 为 gunicorn 指定 wsig 中application 的位置（配置 gunicorn）
#   因为在 wsig 中存在application = get_wsgi_application()
#   注意首先需要进入 项目的路径下，使用包的方式指向该 application
#   (首先确定在Python 的虚拟环境下)
#   gunicorn superlists.wsgi:application
#   配置 STATIC_ROOT
#   执行 collectstatic 指令
#   重启 nginx        sudo systemctl reload  nginx
#   重启 gunicorn     gunicorn superlists.wsgi:application

#   (除了 debug 模式没有关闭, ALLOW_HOST 没有配置)
#   以上完成了 使用 gunicorn 的服务器配置。

#   pip broken by 'NewConnectionError
#   解决这个问题
#   sudo vi /ect/resolv.conf
# nameserver 114.114.114.114
# nameserver 8.8.8.8
#

#  关于使用 fabic3 实现自动部署
#   1: 创建一个文件 fabfile.py 在 deploy_tools 的文件夹下
#   调用方式 fab
