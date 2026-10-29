from django.db import models

TYPES_TRAVAUX = [
    ("corde", "Travaux d'accès difficile sur corde"),
    ("structures", "Structures métalliques"),
    ("soudure", "Soudure"),
    ("bardage", "Bardage & couverture"),
    ("etancheite", "Étanchéité"),
    ("peinture", "Revêtements & peinture"),
    ("lessivage", "Lessivage des façades"),
    ("facade", "Installations en façade"),
    ("maintenance", "Maintenance industrielle"),
    ("autre", "Autre / à préciser"),
]

STATUTS = [
    ("nouvelle", "Nouvelle"),
    ("en_etude", "En étude"),
    ("devis_envoye", "Devis envoyé"),
    ("acceptee", "Acceptée"),
    ("terminee", "Terminée"),
]


class DevisRequest(models.Model):
    """Demande de devis (section 13 du cahier des charges — priorité Très haute)."""

    # Coordonnées
    nom = models.CharField("Nom / entreprise", max_length=150)
    telephone = models.CharField("Téléphone", max_length=30)
    email = models.EmailField("E-mail")

    # Détails du chantier
    localisation = models.CharField("Localisation du chantier", max_length=200)
    type_travaux = models.CharField("Type de travaux", max_length=20, choices=TYPES_TRAVAUX)
    dimensions = models.CharField("Dimensions approximatives", max_length=150, blank=True)
    hauteur = models.CharField("Hauteur de travail", max_length=100, blank=True)
    date_souhaitee = models.DateField("Date souhaitée d'intervention", blank=True, null=True)
    informations_techniques = models.TextField(
        "Informations techniques disponibles", blank=True
    )
    message = models.TextField("Message libre", blank=True)

    # Suivi interne
    statut = models.CharField("Statut", max_length=20, choices=STATUTS, default="nouvelle")
    date_creation = models.DateTimeField("Reçue le", auto_now_add=True)

    class Meta:
        verbose_name = "Demande de devis"
        verbose_name_plural = "Demandes de devis"
        ordering = ["-date_creation"]

    def __str__(self):
        return f"{self.nom} — {self.get_type_travaux_display()}"


def devis_upload_path(instance, filename):
    return f"devis/{instance.devis_id or 'tmp'}/{filename}"


class DevisFichier(models.Model):
    """Photo ou document joint à une demande de devis."""

    devis = models.ForeignKey(DevisRequest, on_delete=models.CASCADE, related_name="fichiers")
    fichier = models.FileField("Fichier", upload_to=devis_upload_path)
    ajoute_le = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Fichier joint"
        verbose_name_plural = "Fichiers joints"

    def __str__(self):
        return self.fichier.name
