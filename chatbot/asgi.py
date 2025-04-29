"""
ASGI config for chatbot project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot.settings')

application = get_asgi_application()
# settings.py
CSRF_TRUSTED_ORIGINS = [
    'https://chatbot-p465.onrender.com',  # Your Render URL
    # Add other domains if needed (e.g., custom domains)
]

# Ensure Render's proxy headers are trusted
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')