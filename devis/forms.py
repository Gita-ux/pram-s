import os

from django import forms
from django.conf import settings

from .models import DevisRequest


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    """Permet de sélectionner plusieurs fichiers dans un seul champ."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput(attrs={"multiple": True}))
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(d, initial) for d in data]
        return single_file_clean(data, initial)


class DevisForm(forms.ModelForm):
    fichiers = MultipleFileField(
        label="Photos ou vidéos du chantier",
        required=False,
        help_text=(
            f"Formats acceptés : {', '.join(settings.ALLOWED_UPLOAD_EXTENSIONS)} — "
            f"{settings.MAX_UPLOAD_SIZE_MB} Mo max par fichier, "
            f"{settings.MAX_UPLOAD_FILES} fichiers max."
        ),
    )

    class Meta:
        model = DevisRequest
        fields = [
            "nom",
            "telephone",
            "email",
            "localisation",
            "type_travaux",
            "dimensions",
            "hauteur",
            "date_souhaitee",
            "informations_techniques",
            "message",
        ]
        widgets = {
            "nom": forms.TextInput(attrs={"placeholder": "Nom / entreprise"}),
            "telephone": forms.TextInput(attrs={"placeholder": "+237 ..."}),
            "email": forms.EmailInput(attrs={"placeholder": "vous@exemple.com"}),
            "localisation": forms.TextInput(attrs={"placeholder": "Ville, quartier, adresse..."}),
            "dimensions": forms.TextInput(attrs={"placeholder": "Ex : façade de 40m x 15m"}),
            "hauteur": forms.TextInput(attrs={"placeholder": "Ex : 25 mètres / R+8"}),
            "date_souhaitee": forms.DateInput(attrs={"type": "date"}),
            "informations_techniques": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Plans, contraintes, accès..."}
            ),
            "message": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Décrivez votre projet..."}
            ),
        }

    def clean_fichiers(self):
        fichiers = self.files.getlist("fichiers")
        if len(fichiers) > settings.MAX_UPLOAD_FILES:
            raise forms.ValidationError(
                f"Vous ne pouvez joindre que {settings.MAX_UPLOAD_FILES} fichiers maximum."
            )
        max_bytes = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
        for f in fichiers:
            ext = os.path.splitext(f.name)[1].lower()
            if ext not in settings.ALLOWED_UPLOAD_EXTENSIONS:
                raise forms.ValidationError(
                    f"Le fichier « {f.name} » n'est pas dans un format autorisé."
                )
            if f.size > max_bytes:
                raise forms.ValidationError(
                    f"Le fichier « {f.name} » dépasse {settings.MAX_UPLOAD_SIZE_MB} Mo."
                )
        return fichiers
