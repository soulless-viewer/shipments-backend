from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = (
        "django-insecure-%_=q)&4lk+uhgye2z0e2p*jvkcj^rf89v$qy=$uvi87@9$jya+"
)

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "rest_framework",
    "corsheaders",
    "shipment",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGIN_REGEXES = []

ROOT_URLCONF = "app.urls"

TEMPLATES = []

WSGI_APPLICATION = "app.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PAGINATION_CLASS": (
        "rest_framework.pagination.PageNumberPagination"
    ),
    "PAGE_SIZE": 6,
}
