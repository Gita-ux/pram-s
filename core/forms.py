from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["nom", "email", "telephone", "sujet", "message"]
        widgets = {
            "nom": forms.TextInput(attrs={"placeholder": "Votre nom"}),
            "email": forms.EmailInput(attrs={"placeholder": "Votre e-mail"}),
            "telephone": forms.TextInput(attrs={"placeholder": "Votre téléphone (optionnel)"}),
            "sujet": forms.TextInput(attrs={"placeholder": "Sujet de votre message"}),
            "message": forms.Textarea(attrs={"placeholder": "Votre message", "rows": 5}),
        }
