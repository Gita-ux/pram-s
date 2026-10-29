from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import DevisForm
from .models import DevisFichier


def devis_request(request):
    """Page 'Demander un devis' (section 13 — priorité Très haute)."""
    if request.method == "POST":
        form = DevisForm(request.POST, request.FILES)
        if form.is_valid():
            devis = form.save()
            for f in form.cleaned_data.get("fichiers", []):
                DevisFichier.objects.create(devis=devis, fichier=f)
            messages.success(
                request,
                "Votre demande de devis a bien été envoyée. "
                "Notre équipe étudiera votre projet et reviendra vers vous rapidement.",
            )
            return redirect("devis:request")
    else:
        form = DevisForm()
    return render(request, "devis/devis.html", {"form": form})
