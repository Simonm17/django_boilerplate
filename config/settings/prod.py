from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
]

INSTALLED_APPS += [
    'storages',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.setdefault('EMAIL_HOST_USER', '')

EMAIL_HOST_PASSWORD = os.environ.setdefault('EMAIL_HOST_PASSWORD', '')


# AWS Settings
AWS_ACCESS_KEY_ID = os.environ.setdefault('AWS_ACCESS_KEY_ID', '')

AWS_SECRET_ACCESS_KEY = os.environ.setdefault('AWS_SECRET_ACCESS_KEY', '')

AWS_STORAGE_BUCKET_NAME = os.environ.setdefault('AWS_STORAGE_BUCKET_NAME', '')

AWS_S3_FILE_OVERWRITE = False

AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


django_heroku.settings(locals())