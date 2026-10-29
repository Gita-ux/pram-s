from django.contrib import admin
from django.utils.html import format_html

from core.admin import pram_admin_site
from .models import Service


@admin.register(Service, site=pram_admin_site)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("numero", "titre", "actif", "image_preview")
    list_editable = ("actif",)
    readonly_fields = ("image_preview",)
    prepopulated_fields = {"slug": ("titre",)}
    ordering = ("numero",)
    list_per_page = 20

    def image_preview(self, obj):
        if not obj.image:
            return "—"
        return format_html(
            '<img src="{}" style="width: 90px; height: 60px; object-fit: cover; border-radius: 6px;" />',
            obj.image.url,
        )

    image_preview.short_description = "Image"
