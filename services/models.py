from django.db import models
from django.urls import reverse


class Service(models.Model):
    """Un domaine d'intervention de PRAM-S (section 9 du cahier des charges)."""

    numero = models.PositiveSmallIntegerField("N°", help_text="Ordre d'affichage (01 à 09...)")
    titre = models.CharField("Titre", max_length=150)
    slug = models.SlugField("Slug", max_length=170, unique=True)
    icone = models.CharField(
        "Icône (classe Bootstrap Icons)",
        max_length=60,
        default="bi-tools",
        help_text="Ex : bi-shield-check — voir icons.getbootstrap.com",
    )
    description_courte = models.CharField("Description courte", max_length=250)
    description_longue = models.TextField("Description détaillée", blank=True)
    prestations = models.TextField(
        "Prestations (une par ligne)",
        blank=True,
        help_text="Chaque ligne devient un élément de liste sur la page du service.",
    )
    image = models.ImageField("Image", upload_to="services/", blank=True, null=True)
    actif = models.BooleanField("Actif", default=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["numero"]

    def __str__(self):
        return f"{self.numero:02d} — {self.titre}"

    def get_absolute_url(self):
        return reverse("services:detail", kwargs={"slug": self.slug})

    def liste_prestations(self):
        return [p.strip() for p in self.prestations.splitlines() if p.strip()]
