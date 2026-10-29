from django.urls import path

from . import views

app_name = "realisations"

urlpatterns = [
    path("", views.realisation_list, name="list"),
    path("<slug:slug>/", views.realisation_detail, name="detail"),
]
