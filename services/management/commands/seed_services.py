from django.core.management.base import BaseCommand
from django.utils.text import slugify

from services.models import Service

SERVICES = [
    {
        "numero": 1,
        "titre": "Travaux d'accès difficile sur corde",
        "icone": "bi-arrow-down-up",
        "description_courte": "Interventions sur structures, façades, bâtiments et installations nécessitant des techniques d'accès sur corde.",
        "prestations": "Travaux en hauteur\nMaintenance sur structures\nInstallation d'équipements\nInspection visuelle\nNettoyage\nRéparation\nIntervention sur zones difficiles d'accès",
    },
    {
        "numero": 2,
        "titre": "Structures métalliques",
        "icone": "bi-bricks",
        "description_courte": "Montage, assemblage et intervention sur structures métalliques.",
        "prestations": "Montage de structures\nAssemblage\nPose de profilés métalliques\nInstallation de portiques\nPose de pannes\nModification de structures\nTravaux de renforcement",
    },
    {
        "numero": 3,
        "titre": "Soudure",
        "icone": "bi-lightning-charge",
        "description_courte": "Travaux de soudure et d'assemblage métallique.",
        "prestations": "Soudure sur structures\nRéparation métallique\nAssemblage\nRenforcement\nTravaux de maintenance",
    },
    {
        "numero": 4,
        "titre": "Bardage & couverture",
        "icone": "bi-building",
        "description_courte": "Pose, maintenance et intervention en hauteur sur bardage et couverture.",
        "prestations": "Pose de bardage\nMaintenance de bardage\nRéparation\nFixation d'éléments\nIntervention sur couverture\nTravaux en hauteur",
    },
    {
        "numero": 5,
        "titre": "Étanchéité",
        "icone": "bi-droplet",
        "description_courte": "Étanchéité à froid et à chaud sur toutes surfaces.",
        "prestations": "Étanchéité à froid\nÉtanchéité à chaud\nRéparation de zones dégradées\nTraitement des infiltrations\nIntervention sur gouttières et surfaces techniques",
    },
    {
        "numero": 6,
        "titre": "Revêtement & peinture",
        "icone": "bi-paint-bucket",
        "description_courte": "Préparation et application de revêtements de protection.",
        "prestations": "Préparation des surfaces\nPeinture\nRevêtement\nProtection des structures\nTravaux de finition",
    },
    {
        "numero": 7,
        "titre": "Lessivage de façades",
        "icone": "bi-water",
        "description_courte": "Nettoyage de façades vitrées, alucobond et surfaces carrelées.",
        "prestations": "Vitrages\nAlucobond\nCarrelage\nFaçades d'immeubles\nSurfaces difficiles d'accès",
    },
    {
        "numero": 8,
        "titre": "Installations en façade",
        "icone": "bi-signpost",
        "description_courte": "Enseignes, panneaux, LED et équipements en hauteur.",
        "prestations": "Enseignes publicitaires\nPanneaux\nÉclairage LED\nÉquipements techniques\nSupports\nFixations diverses",
    },
    {
        "numero": 9,
        "titre": "Maintenance industrielle",
        "icone": "bi-gear-wide-connected",
        "description_courte": "Interventions techniques et maintenance industrielle.",
        "prestations": "Maintenance corrective\nRéparations\nTravaux métalliques\nIntervention sur structures\nTravaux en hauteur\nMaintenance d'équipements et installations",
    },
]


class Command(BaseCommand):
    help = "Crée ou met à jour les 9 services de PRAM-S définis dans le cahier des charges."

    def handle(self, *args, **options):
        for data in SERVICES:
            slug = slugify(data["titre"])
            service, created = Service.objects.update_or_create(
                slug=slug,
                defaults={**data},
            )
            action = "créé" if created else "mis à jour"
            self.stdout.write(self.style.SUCCESS(f"Service {action} : {service}"))
        self.stdout.write(self.style.SUCCESS("Terminé — 9 services disponibles."))
