import os
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(dotenv.find_dotenv())


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-nxjvm_=1vo=io18_+vz1ott6uu2qm(=6f#!#aemnwtwwppt*@e"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get("DEBUGDB") == "False" else True

ALLOWED_HOSTS = ["web-production-2e20.up.railway.app", "127.0.0.1"]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1",
    "https://web-production-2e20.up.railway.app",
]


# Application definition

INSTALLED_APPS = [
    "jazzmin",  # Theme
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # My apps
    "bookguardian",
    "userauths",
    # allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.environ.get("CLIENT_ID"),
            "secret": os.environ.get("SECRET"),
            "key": "",
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
    },
}


ROOT_URLCONF = "setup.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "setup.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE"),
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "userauths.User"

SOCIALACCOUNT_PIPELINE = (
    "allauth.socialaccount.pipeline.social_login",
    "userauths.pipeline.link_to_existing_user",
    "allauth.socialaccount.pipeline.social_user",
    "allauth.socialaccount.pipeline.associate_user",
    "allauth.socialaccount.pipeline.load_extra_data",
    "allauth.socialaccount.pipeline.user.create_user",
    "allauth.socialaccount.pipeline.save_social_token",
    "allauth.socialaccount.pipeline.social_account",
    "allauth.socialaccount.pipeline.sync_user_profile",
)

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LOGIN_URL = "userauths:sign-in"
LOGIN_REDIRECT_URL = "bookguardian:index"
LOGOUT_REDIRECT_URL = "bookguardian:ladinpage"

SITE_ID = 1

# STORAGES = {
#     "default": {
#         "BACKEND": "django.core.files.storage.FileSystemStorage",
#     },
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

#
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "templates/static")]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.environ.get("RAILWAY_VOLUME_MOUNT_PATH")


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# if DEBUG == True:
#     EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# else:
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_POST = os.environ.get("EMAIL_POST")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
