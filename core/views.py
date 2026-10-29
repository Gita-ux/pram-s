from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render

from realisations.models import Realisation
from services.models import Service

from .forms import ContactForm


def home(request):
    """Page d'accueil (section 7 du cahier des charges)."""
    services = Service.objects.filter(actif=True).order_by("numero")
    realisations = Realisation.objects.filter(publie=True)[:6]
    context = {
        "services": services,
        "realisations": realisations,
    }
    return render(request, "core/home.html", context)


def about(request):
    """Page À propos (section 8)."""
    return render(request, "core/about.html")


def security(request):
    """Page Sécurité (section 11)."""
    return render(request, "core/security.html")


def contact(request):
    """Page Contact avec formulaire (section 14)."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                send_mail(
                    subject=f"[Site PRAM-S] Nouveau message — {form.cleaned_data['sujet'] or 'Contact'}",
                    message=(
                        f"Nom : {form.cleaned_data['nom']}\n"
                        f"E-mail : {form.cleaned_data['email']}\n"
                        f"Téléphone : {form.cleaned_data['telephone']}\n\n"
                        f"{form.cleaned_data['message']}"
                    ),
                    from_email=None,
                    recipient_list=[settings.CONTACT_EMAIL_RECIPIENT],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(
                request,
                "Votre message a bien été envoyé. Notre équipe vous recontactera rapidement.",
            )
            return redirect("core:contact")
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form})
