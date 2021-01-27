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
1. Secret key
2. Postgres Password
3. Email Host User & Password
4. Social Account Providers App Client ID's & Secret Keys (Make sure to set up your Google OAuth2 under Google API's "Credential" tab)

If error when pip install psycopg2, try pip install psycopg2-binary.

###
- If you need to use a custom user model, you can use the provided Users app to set up.
- You also have the option to place your app templates into the app directory itself or use the main templates folder; I left that pretty flexible.

- Should you have any questions or concerns, please feel free to email me at ryanchuung@gmail.com