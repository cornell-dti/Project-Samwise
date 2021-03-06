import os

SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(32))
COLORS = ['4286f4', 'ed4040', 'd33fed', '17b236', '17c2ed']

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
REDIRECT_URI = '%s/gauth_callback' % (os.getenv('CALLBACK_URI', 'http://localhost:5000'))
AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
SCOPE = ['email', 'https://www.googleapis.com/auth/calendar.readonly']

SQLALCHEMY_DATABASE_URI = 'postgres://{user}:{password}@{host}:5432/{dbname}'.format(
    user=os.getenv('SAMWISE_USERNAME'),
    password=os.getenv('SAMWISE_PASSWORD'),
    host=os.getenv('SAMWISE_DB'),
    dbname=os.getenv('SAMWISE_DBNAME'))
