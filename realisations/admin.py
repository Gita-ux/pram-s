from django.contrib import admin

from core.admin import pram_admin_site
from .models import Realisation, RealisationImage


class RealisationImageInline(admin.TabularInline):
    model = RealisationImage
    extra = 1


@admin.register(Realisation, site=pram_admin_site)
class RealisationAdmin(admin.ModelAdmin):
    list_display = ("titre", "categorie", "localisation", "date_realisation", "publie")
    list_filter = ("categorie", "publie")
    list_editable = ("publie",)
    prepopulated_fields = {"slug": ("titre",)}
    inlines = [RealisationImageInline]
    ordering = ("-date_realisation", "-id")
    list_per_page = 20
