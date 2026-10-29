"""
Django settings for pram_s project.
Site vitrine PRAM-S — Pro Rope Access Multi
"""

import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-p^r6^)@w6#=5w@fzrtj@_a1c1i0#8jsvzs3+_9(-4=zm(uv6#i",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost,192.168.66.60"
).split(",")

# Render fournit automatiquement cette variable (ex: pram-s-site.onrender.com)
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Nécessaire pour que les formulaires (devis, contact, connexion) fonctionnent en HTTPS
CSRF_TRUSTED_ORIGINS = [
    f"https://{host}" for host in ALLOWED_HOSTS
    if host not in ("127.0.0.1", "localhost") and not host.startswith("192.168.")
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps du projet PRAM-S
    "core",
    "services",
    "realisations",
    "devis",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pram_s.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Contexte global : coordonnées de l'entreprise disponibles partout
                "core.context_processors.site_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "pram_s.wsgi.application"


# Database
# En local : SQLite (aucune configuration). Sur Render : PostgreSQL via DATABASE_URL.
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "Africa/Douala"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Fichiers médias (photos de réalisations, pièces jointes des devis...)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email (console en dev — à remplacer par un vrai backend SMTP en production)
EMAIL_BACKEND = os.environ.get(
    "DJANGO_EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend"
)
EMAIL_HOST = os.environ.get("DJANGO_EMAIL_HOST", "")
EMAIL_PORT = int(os.environ.get("DJANGO_EMAIL_PORT", 587))
EMAIL_HOST_USER = os.environ.get("DJANGO_EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("DJANGO_EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = True
CONTACT_EMAIL_RECIPIENT = os.environ.get("CONTACT_EMAIL_RECIPIENT", "contact@pram-s.cm")

# Limites d'upload pour le formulaire de devis (section 21 du cahier des charges)
MAX_UPLOAD_SIZE_MB = 8
ALLOWED_UPLOAD_EXTENSIONS = [".jpg", ".jpeg", ".png", ".webp", ".pdf"]
MAX_UPLOAD_FILES = 6

# Redirection après connexion à l'admin
LOGIN_REDIRECT_URL = "/admin/"

# --- Informations de l'entreprise (à compléter par PRAM-S — section 31 du CDC) ---
COMPANY_INFO = {
    "name": "PRAM-S",
    "full_name": "Pro Rope Access Multi",
    "slogan": "Le détail fait la différence.",
    "phone": "+237 XX XX XX XX",
    "whatsapp": "237XXXXXXXXX",  # format international sans "+" pour le lien wa.me
    "email": "contact@pram-s.cm",
    "zone": "Cameroun — interventions possibles selon le projet",
    "facebook": "#",
    "instagram": "#",
    "linkedin": "#",
    "tiktok": "#",
}
