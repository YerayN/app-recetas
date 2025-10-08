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

# Detectar si estamos en producción
# ⚠️ CAMBIO: Detectar por múltiples métodos
IS_PRODUCTION = (
    os.getenv("RAILWAY_ENVIRONMENT") is not None or
    os.getenv("RAILWAY_PROJECT_ID") is not None or
    "railway.app" in os.getenv("RAILWAY_PUBLIC_DOMAIN", "")
)

# 🐛 DEBUG: Imprimir para verificar
print(f"🔍 IS_PRODUCTION: {IS_PRODUCTION}")
print(f"🔍 RAILWAY_ENVIRONMENT: {os.getenv('RAILWAY_ENVIRONMENT')}")
print(f"🔍 RAILWAY_PROJECT_ID: {os.getenv('RAILWAY_PROJECT_ID')}")

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

# ✅ CORS - Orígenes permitidos
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://app-recetas-front.vercel.app",
]

# Permitir todos los subdominios vercel.app (para previews)
CORS_ALLOWED_ORIGIN_REGEXES = [r"^https://.*\.vercel\.app$"]

# CSRF - Orígenes confiables
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://app-recetas-front.vercel.app",
    "https://app-recetas-production.up.railway.app",
]

# ⚠️ CRÍTICO: Permitir credenciales (cookies)
CORS_ALLOW_CREDENTIALS = True

# ⚠️ CRÍTICO: Configuración de cookie CSRF
CSRF_COOKIE_SECURE = IS_PRODUCTION  # True en producción (HTTPS), False en local
CSRF_COOKIE_HTTPONLY = False  # ⚠️ DEBE SER FALSE para que JS pueda leerla
CSRF_COOKIE_SAMESITE = 'None' if IS_PRODUCTION else 'Lax'
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_COOKIE_DOMAIN = None  # ⚠️ Dejarlo en None para que funcione cross-domain

# 🐛 DEBUG: Imprimir configuración CSRF
print(f"🔍 CSRF_COOKIE_SECURE: {CSRF_COOKIE_SECURE}")
print(f"🔍 CSRF_COOKIE_SAMESITE: {CSRF_COOKIE_SAMESITE}")
print(f"🔍 CSRF_COOKIE_HTTPONLY: {CSRF_COOKIE_HTTPONLY}")

# Configuración de cookie de sesión
SESSION_COOKIE_SECURE = IS_PRODUCTION
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'None' if IS_PRODUCTION else 'Lax'
SESSION_COOKIE_DOMAIN = None  # ⚠️ Dejarlo en None

# 👇 Muy importante para Railway detrás de proxy HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ------------------------------------------------
# ⚙️ REST FRAMEWORK CONFIG
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
# ⚙️ LOGGING (opcional, para depurar)
# ------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}