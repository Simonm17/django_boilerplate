# Django Allauth Demo

- Django boilerplate website that uses Django all-auth for authentication
- Includes registration and social authentication (via Google)

## Main packages
- Django 3.1
- Django all-auth 0.32.0
- Django Debug Toolbar 3.2
- Crispy Forms 1.9
- Sentry

## Environment Variable Configurations
base.py:
1. DJANGO_SENTRY_SDN
2. SECRET_KEY
3. PSQL_NAME
4. PSQL_PASS
- GOOGLE_AUTH_CLIENT
- GOOGLE_AUTH_SECRET

prod.py
4. EMAIL_HOST_USER
5. EMAIL_HOST_PASSWORD
6. AWS_ACCESS_KEY_ID
7. AWS_SECRET_ACCESS_KEY
8. AWS_STORAGE_BUCKET_NAME


###
- If you have trouble with User's initial migrations, run "python manage.py makemigrations users" first, then migrate.

- Should you have any questions or concerns, please feel free to email me at ryanchuung@gmail.com