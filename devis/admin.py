from django.contrib import admin

from core.admin import pram_admin_site
from .models import DevisFichier, DevisRequest


class DevisFichierInline(admin.TabularInline):
    model = DevisFichier
    extra = 0
    readonly_fields = ("fichier", "ajoute_le")
    can_delete = False


@admin.register(DevisRequest, site=pram_admin_site)
class DevisRequestAdmin(admin.ModelAdmin):
    list_display = ("nom", "type_travaux", "localisation", "statut", "date_creation")
    list_filter = ("statut", "type_travaux")
    list_editable = ("statut",)
    search_fields = ("nom", "email", "telephone", "localisation")
    inlines = [DevisFichierInline]
    readonly_fields = ("date_creation",)
    ordering = ("-date_creation",)
    list_per_page = 20
