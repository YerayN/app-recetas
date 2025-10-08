"""
Django settings for recetas_backend project.
Configurado para desarrollo local y despliegue en Railway + Vercel.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------
# ⚙️ CONFIGURACIÓN GENERAL
# ------------------------------------------------
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-i_p1i2^38s0+%_*77=an+um$n1vg8wytafm6nm-#uszv67shlw"
)
DEBUG = os.getenv("DEBUG", "True") == "True"

# Railway y Vercel pasarán estos valores por variables de entorno
ALLOWED_HOSTS = [
    "app-recetas-production.up.railway.app",
    "localhost",
    "127.0.0.1",
]

# ------------------------------------------------
# 📦 APLICACIONES
# ------------------------------------------------
INSTALLED_APPS = [
    # Django base
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Terceros
    "rest_framework",
    "corsheaders",

    # App propia
    "recetas",
]

# ------------------------------------------------
# 🧩 MIDDLEWARE
# ------------------------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # ⚠️ importante: arriba del todo
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "recetas_backend.urls"

# ------------------------------------------------
# 🧠 TEMPLATES
# ------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "recetas_backend.wsgi.application"

# ------------------------------------------------
# 🗃️ BASE DE DATOS
# ------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ------------------------------------------------
# 🔐 VALIDACIÓN DE CONTRASEÑAS
# ------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ------------------------------------------------
# 🌍 INTERNACIONALIZACIÓN
# ------------------------------------------------
LANGUAGE_CODE = "es-es"
TIME_ZONE = "Europe/Madrid"
USE_I18N = True
USE_TZ = True

# ------------------------------------------------
# 🖼️ ARCHIVOS ESTÁTICOS
# ------------------------------------------------
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------------------------------------------
# 🔄 CORS / CSRF (React frontend)
# ------------------------------------------------

def _split_env(name, default_list=None):
    value = os.getenv(name)
    if not value:
        return default_list or []
    return [v.strip() for v in value.split(",") if v.strip()]

# 🚫 Quita esto en producción: CORS_ALLOW_ALL_ORIGINS
# CORS_ALLOW_ALL_ORIGINS = True  # ❌ desactivado por seguridad

# ✅ CORS y CSRF correctos
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://app-recetas-front.vercel.app",
]

# Permitir todos los subdominios vercel.app (para previews)
CORS_ALLOWED_ORIGIN_REGEXES = [r"^https://.*\.vercel\.app$"]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://app-recetas-front.vercel.app",
    "https://app-recetas-production.up.railway.app",
    "https://*.vercel.app",
]

# Configuración de cookies cross-domain
CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = None
CSRF_COOKIE_SECURE = True

# 👇 Muy importante para Railway detrás de proxy HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ------------------------------------------------
# ⚙️ REST FRAMEWORK CONFIG
# ------------------------------------------------
REST_FRAMEWORK = {
    # ❌ ESTABA VACÍA: "DEFAULT_AUTHENTICATION_CLASSES": [],
    # ✅ AÑADIR SESSION AUTHENTICATION
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication", 
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_FILTER_BACKENDS": ["rest_framework.filters.SearchFilter"],
}

# ------------------------------------------------
# 💾 LOGIN / LOGOUT
# ------------------------------------------------
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# ------------------------------------------------
# ⚙️ LOGGING (opcional, para depurar)
# ------------------------------------------------
if DEBUG:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {"console": {"class": "logging.StreamHandler"}},
        "root": {"handlers": ["console"], "level": "DEBUG"},
    }
