import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--yyujb9j%u97+x1_gz%p_4oizkw9@27xefc$49lp8w-l=dctgp'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'rest_framework',
    'corsheaders',
    'users',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oidc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'oidc.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# My Variable
CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/admin/login/'

# with open('oidc.pub', 'rb') as PRIVATE_KEY:
#     print(str(PRIVATE_KEY.read()))
#     os.environ['OIDC_RSA_PRIVATE_KEY'] = str(PRIVATE_KEY.read())

os.environ['OIDC_RSA_PRIVATE_KEY'] = '''-----BEGIN PRIVATE KEY-----
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
A3w0kCN7t0Z3jipfZnk/8+g6AdP9bA==
-----END PRIVATE KEY-----'''

OAUTH2_PROVIDER = {
    "OIDC_ENABLED": True,
    "PKCE_REQUIRED": False,
    "OIDC_RSA_PRIVATE_KEY": os.environ.get("OIDC_RSA_PRIVATE_KEY"),
    "SCOPES": {
        "openid": "OpenID Connect scope",
        "profile": "Profile scope",
        "email": "Email scope",
        "read": "Read scope",
        "write": "Write scope",
        "address": "Address Scope",
        "phone": "Phone Number Scope",
        "permissions": "Permissions",
        'type': 'User Type',
        'groups': 'Access to your groups',
    },
    "OAUTH2_VALIDATOR_CLASS": "oidc.oauth_validator.CustomOAuth2Validator",
    "ACCESS_TOKEN_EXPIRE_SECONDS": 2592000,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

STATIC_ROOT = "static"

# id: CSTT8X712gn5tbKrBeN9AT5d92nZ2hi6yY0N90ES
# sec: 5uCoRaAiObp3xjeznggqAiQ7LRbGNggAo0J3uP0ufQf1InSuLtLKgWw8LaNVGZYyyNd0zZWTRlQIOR17dmSY1kmBlJg8vYSRLUUedyhQEKFPcvPdd1FTCj0zqMWRZ5t9
# Bahis Serve
# Id: MOkxIl8tFCO3ZitgrFLqlRvJ9EgoN7mcyUddPtJI
# sec: gbjNip2Q4w5qNIPVbWTjMfN2ZpXYxYCGHS60l2uOmtPmwbyPxpStz4bQhkmZsdtGKChuIxKc5egOVXx3q2IHk6x5eLW0gEucD4Onq86LPzcXPzGpOJggl31ujUbixpuY
# curl -X POST -d "grant_type=password&username=sharful&password=321" -u "MOkxIl8tFCO3ZitgrFLqlRvJ9EgoN7mcyUddPtJI:gbjNip2Q4w5qNIPVbWTjMfN2ZpXYxYCGHS60l2uOmtPmwbyPxpStz4bQhkmZsdtGKChuIxKc5egOVXx3q2IHk6x5eLW0gEucD4Onq86LPzcXPzGpOJggl31ujUbixpuY" http://localhost:8000/token/
# Bahis desk
# Id: L8Jnuho9AkCEBdpFQMMJsJBBb1Dqgt26EEzxCRWo
# sec: Jfi4A4Kf4nqmlbGwaqSDDN3nDd1hePuRfgCcZKfIyojmmg8WN2wBcnvxcUZ56bFNOhyIG6HEP7UzzryjnTt6Gd5u6oEezn0OmLQRef0gyPm0eLSUzre7tvEImUSYAKib


