# Site vitrine PRAM-S — Pro Rope Access Multi

Site web vitrine développé avec **Python / Django**, conçu à partir du cahier des
charges fourni et de la maquette de design.

## 1. Installation (dans VS Code)

Ouvre le dossier `pram-s` dans VS Code, puis dans le terminal intégré (`Ctrl+ù` ou `Ctrl+backtick`) :

```bash
# 1. Créer un environnement virtuel
python -m venv venv

# 2. L'activer
# Windows :
venv\Scripts\activate
# macOS / Linux :
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Appliquer les migrations (création de la base de données)
python manage.py migrate

# 5. Charger les 9 services par défaut (définis dans le cahier des charges)
python manage.py seed_services

# 6. Créer ton compte administrateur
python manage.py createsuperuser

# 7. Lancer le serveur de développement
python manage.py runserver
```

Le site est accessible sur **http://127.0.0.1:8000/**
et l'administration sur **http://127.0.0.1:8000/admin/**

> Astuce VS Code : installe l'extension officielle **Python** (Microsoft) et
> sélectionne l'interpréteur `venv` (palette de commandes → *Python: Select Interpreter*).

## 2. Structure du projet

```
pram-s/
├── manage.py
├── pram_s/          → configuration du projet (settings, urls)
├── core/            → accueil, à propos, sécurité, contact
├── services/        → les 9 domaines d'intervention
├── realisations/    → portfolio de chantiers (avant/pendant/après)
├── devis/           → formulaire de demande de devis + fichiers joints
├── templates/       → tous les fichiers HTML
├── static/
│   ├── css/style.css   → design complet du site
│   └── js/main.js      → animations et interactions
└── media/           → photos uploadées (services, réalisations, devis)
```

## 3. Ce qui est déjà fonctionnel

- ✅ Toutes les pages du cahier des charges : Accueil, À propos, Services (liste +
  détail), Réalisations (liste filtrable + détail avec galerie avant/pendant/après),
  Sécurité, Demander un devis, Contact.
- ✅ Formulaire de **contact** (enregistré en base + tentative d'envoi d'e-mail).
- ✅ Formulaire de **demande de devis** avec upload de plusieurs photos/vidéos,
  suivi de statut (Nouvelle → En étude → Devis envoyé → Acceptée → Terminée).
- ✅ Espace d'administration Django (`/admin/`) pour gérer services, réalisations,
  demandes de devis et messages, sans toucher au code.
- ✅ Design sombre premium avec accent doré, repris de la maquette fournie.
- ✅ Animations légères : apparition au défilement, compteurs animés, menu mobile,
  en-tête qui se fige au scroll, effets de survol.
- ✅ Boutons flottants WhatsApp et appel téléphonique.
- ✅ Site responsive (mobile, tablette, ordinateur).
- ✅ Base SEO : balises title/description par page, structure H1/H2/H3, URLs propres.

## 4. Ce qu'il te reste à personnaliser

Ce sont les éléments listés en section 31 du cahier des charges, à fournir par PRAM-S :

1. **Coordonnées réelles** : dans `pram_s/settings.py`, complète le dictionnaire
   `COMPANY_INFO` (téléphone, WhatsApp, e-mail, réseaux sociaux).
2. **Logo et couleurs officielles** : si PRAM-S fournit un logo, remplace le bloc
   `.brand__mark` dans `templates/base.html` par une image, et ajuste les variables
   de couleur en haut de `static/css/style.css` si besoin.
3. **Vraies photos** : toutes les images sont actuellement des **placeholders**
   (`placehold.co`) à remplacer par de vraies photos de chantiers/techniciens, à
   ajouter :
   - Services → depuis `/admin/services/service/`
   - Réalisations → depuis `/admin/realisations/realisation/`
   - Bannière d'accueil → remplace les URLs `https://placehold.co/...` dans
     `templates/core/home.html`
4. **Nom de domaine et hébergement** : à définir avec PRAM-S (section 23 du CDC).
5. **Envoi d'e-mail réel** : configure `DJANGO_EMAIL_HOST`, `DJANGO_EMAIL_HOST_USER`,
   `DJANGO_EMAIL_HOST_PASSWORD` (variables d'environnement, voir `.env.example`)
   avec un vrai fournisseur SMTP.

## 5. Ajouter du contenu (services, réalisations)

Tout se gère depuis l'espace d'administration `/admin/` — aucune connaissance en
code n'est nécessaire pour PRAM-S au quotidien :

- **Services** : modifier titre, description, icône (voir la liste sur
  [icons.getbootstrap.com](https://icons.getbootstrap.com)), prestations.
- **Réalisations** : ajouter un chantier avec image principale, catégorie,
  localisation, puis ajouter des photos avant/pendant/après dans la section
  "Photos de réalisation" en bas du formulaire.
- **Demandes de devis** : consulter, changer le statut, télécharger les fichiers
  envoyés par le client.

## 6. Avant la mise en ligne (checklist sécurité — section 21 du CDC)

- [ ] Mettre `DJANGO_DEBUG=False`
- [ ] Définir une vraie `DJANGO_SECRET_KEY` (variable d'environnement)
- [ ] Renseigner `DJANGO_ALLOWED_HOSTS` avec le vrai nom de domaine
- [ ] Activer HTTPS (certificat SSL chez l'hébergeur)
- [ ] Changer le mot de passe administrateur par défaut
- [ ] Faire des sauvegardes régulières de `db.sqlite3` (ou migrer vers PostgreSQL,
      recommandé en production — voir la configuration `DATABASES` dans `settings.py`)

## 7. Déploiement

Le site est prêt pour un hébergement compatible Django (ex. Render, Railway,
PythonAnywhere, VPS avec Gunicorn + Nginx). Avant de déployer :

```bash
python manage.py collectstatic
```

Cela regroupe tous les fichiers statiques dans `staticfiles/`, à servir par ton
serveur web (Nginx, WhiteNoise, etc.).

---

**PRAM-S — Le détail fait la différence.**
