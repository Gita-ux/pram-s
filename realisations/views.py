from django.shortcuts import get_object_or_404, render

from .models import CATEGORIES, Realisation


def realisation_list(request):
    categorie = request.GET.get("categorie")
    realisations = Realisation.objects.filter(publie=True)
    if categorie:
        realisations = realisations.filter(categorie=categorie)
    return render(
        request,
        "realisations/list.html",
        {
            "realisations": realisations,
            "categories": CATEGORIES,
            "categorie_active": categorie,
        },
    )


def realisation_detail(request, slug):
    realisation = get_object_or_404(Realisation, slug=slug, publie=True)
    return render(request, "realisations/detail.html", {"realisation": realisation})
