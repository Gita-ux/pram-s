"""
URLs racine du projet PRAM-S.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from core.admin import pram_admin_site

urlpatterns = [
    path("admin/", pram_admin_site.urls),
    path("", include("core.urls")),
    path("services/", include("services.urls")),
    path("realisations/", include("realisations.urls")),
    path("devis/", include("devis.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
