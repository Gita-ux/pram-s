"""
Rend les informations de l'entreprise (téléphone, WhatsApp, e-mail...)
disponibles dans TOUS les templates, sans avoir à les repasser dans
chaque vue (utile pour le header, le footer et les boutons flottants).
"""
from django.conf import settings


def site_settings(request):
    return {
        "company": settings.COMPANY_INFO,
    }
