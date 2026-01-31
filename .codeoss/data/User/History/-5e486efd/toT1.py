from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-t@spei%c&+4@2x(wj58r-049rx%fly1jlv$*$!dbo^ifun0%&x')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
ALLOWED_HOSTS = ['*']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core', 
    'clients',
    'bpo_docs',
    'masters',
    'logs',
    'frontend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'ja'

# タイムゾーン（日本の時間にする設定）
TIME_ZONE = 'Asia/Tokyo'
# settings.py の一番下あたりに追加
# 対応する言語のリスト
LANGUAGES = [
    ('en', _('English')),
    ('ja', _('Japanese')),
    ('vi', _('Vietnamese')), # ベトナム語も視野に入れておきます
]

# 翻訳ファイルを置く場所を指定
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

USE_X_FORWARDED_HOST = True # This is fine, but often placed with other security settings.

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
# ログイン成功後にリダイレクトするURL（トップページなど）
LOGIN_REDIRECT_URL = 'menu'

# ログアウト後にリダイレクトするURL（ログイン画面に戻すのが一般的）
LOGOUT_REDIRECT_URL = '/accounts/login/'

CSRF_TRUSTED_ORIGINS = ['https://*.cloudshell.dev']
# Cloud Shellやロードバランサ環境で、httpsを正しく認識させる設定
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
