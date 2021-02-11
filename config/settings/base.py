import os
from pathlib import Path

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    # Make sure to configure your own sdn project key.
    dsn=os.environ.get('DJANGO_SENTRY_SDN'),
    integrations=[DjangoIntegration()],

    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS = [
    # Django contrib
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Allauth packages
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # uncomment to use Google OAuth2 login
    # 'allauth.socialaccount.providers.google',

    # Other 3rd party packages
    'crispy_forms',

    # Django apps
    'users.apps.UsersConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj_social',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('PSQL_PASS'),
        'HOST': 'localhost',
        'PORT': '5432'
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.abspath(os.path.join(BASE_DIR, 'static')),
    # BASE_DIR / "static",  # same thing as above
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_URL = 'account_login'

LOGIN_REDIRECT_URL = '/'

# Allauth settings
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# SOCIALACCOUNT_PROVIDERS = {
    # Set up your google credentials at https://console.developers.google.com/apis/credentials
    # URI: http://127.0.0.1:8000 in development
    # Redirect URI: http://127.0.0.1:8000/accounts/google/login/callback/ in development
#     'google': {
#         'APP': {
#             'client_id': os.environ.get('GOOGLE_AUTH_CLIENT'),
#             'secret': os.environ.get('GOOGLE_AUTH_SECRET'),
#             'key': ''
#         }
#     }
# }

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_SESSION_REMEMBER = True

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_MAX_EMAIL_ADDRESSES = 3

ACCOUNT_USERNAME_BLACKLIST = [
    'admin',
    'staff',
]

# Replacing login/signup forms with custom forms to modify form labels
ACCOUNT_FORMS = {
    "login": "users.forms.CustomLoginForm",
    "signup": "users.forms.CustomSignupForm",
    "add_email": "allauth.account.forms.AddEmailForm",
    "change_password": "allauth.account.forms.ChangePasswordForm",
    "set_password": "allauth.account.forms.SetPasswordForm",
    "reset_password": "allauth.account.forms.ResetPasswordForm",
    "reset_password_from_key": "allauth.account.forms.ResetPasswordKeyForm",
    "disconnect": "allauth.socialaccount.forms.DisconnectForm",
}

