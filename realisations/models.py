from django.db import models
from django.urls import reverse

CATEGORIES = [
    ("corde", "Travaux sur corde"),
    ("bardage", "Bardage"),
    ("publicite", "Installations publicitaires"),
    ("structures", "Structures métalliques"),
    ("etancheite", "Étanchéité"),
    ("maintenance", "Maintenance industrielle"),
]


class Realisation(models.Model):
    """Un chantier réalisé par PRAM-S (section 10 du cahier des charges)."""

    titre = models.CharField("Nom du projet", max_length=150)
    slug = models.SlugField("Slug", max_length=170, unique=True)
    categorie = models.CharField("Catégorie", max_length=20, choices=CATEGORIES)
    localisation = models.CharField("Localisation", max_length=150, blank=True)
    description = models.TextField("Description", blank=True)
    image_principale = models.ImageField("Image principale", upload_to="realisations/")
    informations_complementaires = models.TextField(
        "Informations complémentaires", blank=True
    )
    date_realisation = models.DateField("Date de réalisation", blank=True, null=True)
    publie = models.BooleanField("Publié", default=True)

    class Meta:
        verbose_name = "Réalisation"
        verbose_name_plural = "Réalisations"
        ordering = ["-date_realisation", "-id"]

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("realisations:detail", kwargs={"slug": self.slug})


class RealisationImage(models.Model):
    """Photo complémentaire (avant / pendant / après) d'une réalisation."""

    ETAPE_CHOICES = [
        ("avant", "Avant"),
        ("pendant", "Pendant"),
        ("apres", "Après"),
        ("autre", "Autre"),
    ]

    realisation = models.ForeignKey(
        Realisation, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField("Image", upload_to="realisations/galerie/")
    etape = models.CharField("Étape", max_length=10, choices=ETAPE_CHOICES, default="autre")
    legende = models.CharField("Légende", max_length=150, blank=True)

    class Meta:
        verbose_name = "Photo de réalisation"
        verbose_name_plural = "Photos de réalisation"

    def __str__(self):
        return f"{self.realisation.titre} — {self.get_etape_display()}"
