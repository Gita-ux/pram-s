from django.db import models


class ContactMessage(models.Model):
    """Message envoyé depuis la page Contact (section 14 du cahier des charges)."""

    nom = models.CharField("Nom", max_length=150)
    email = models.EmailField("E-mail")
    telephone = models.CharField("Téléphone", max_length=30, blank=True)
    sujet = models.CharField("Sujet", max_length=200, blank=True)
    message = models.TextField("Message")
    date_envoi = models.DateTimeField("Reçu le", auto_now_add=True)
    lu = models.BooleanField("Lu", default=False)

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ["-date_envoi"]

    def __str__(self):
        return f"{self.nom} — {self.sujet or 'sans sujet'}"
