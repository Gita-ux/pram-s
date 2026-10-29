from django.contrib import admin

from .models import ContactMessage


class PRAMAdminSite(admin.AdminSite):
    site_title = "PRAM-S Admin"
    site_header = "PRAM-S Administration"
    index_title = "Tableau de bord"
    index_template = "admin/custom_index.html"


pram_admin_site = PRAMAdminSite(name="pram_admin")


@admin.register(ContactMessage, site=pram_admin_site)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "sujet", "date_envoi", "lu")
    list_filter = ("lu", "date_envoi")
    search_fields = ("nom", "email", "message")
    readonly_fields = ("date_envoi",)
    list_per_page = 20
