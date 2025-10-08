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

# Detectar entorno Railway (producción)
IS_PRODUCTION = (
    os.getenv("RAILWAY_ENVIRONMENT") is not None
    or "railway.app" in os.getenv("RAILWAY_PUBLIC_DOMAIN", "")
)

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
# 🔄 CORS / CSRF (Frontend React en Vercel)
# ------------------------------------------------

# Frontend en producción
FRONTEND_URL = "https://app-recetas-front.vercel.app"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    FRONTEND_URL,
]

# Permitir previews y subdominios vercel.app
CORS_ALLOWED_ORIGIN_REGEXES = [r"^https://.*\.vercel\.app$"]

# CSRF: dominios de confianza
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    FRONTEND_URL,
]

# ✅ Enviar cookies de sesión y CSRF al frontend
CORS_ALLOW_CREDENTIALS = True

# Cookies seguras cross-domain
SESSION_COOKIE_SECURE = IS_PRODUCTION
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "None" if IS_PRODUCTION else "Lax"
SESSION_COOKIE_DOMAIN = None  # None → usa dominio del backend

CSRF_COOKIE_SECURE = IS_PRODUCTION
CSRF_COOKIE_HTTPONLY = False  # JS necesita leerla
CSRF_COOKIE_SAMESITE = "None" if IS_PRODUCTION else "Lax"
CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_DOMAIN = None

# 🔒 Requerido para que Railway respete HTTPS detrás de proxy
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ------------------------------------------------
# ⚙️ REST FRAMEWORK
# ------------------------------------------------
REST_FRAMEWORK = {
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
# ⚙️ LOGGING
# ------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}
