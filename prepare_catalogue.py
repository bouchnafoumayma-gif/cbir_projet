import os
import csv
import random

# --- Réglages ---
DOSSIER_IMAGES = "static/images"
FICHIER_CSV = "data/catalogue.csv"
EXTENSIONS = (".jpg", ".jpeg", ".png")

# Fourchette de prix (min, max) selon la catégorie
PRIX = {
    "mode": (15, 120),
    "electronique": (50, 900),
    "beaute": (8, 80),
    "jouets": (10, 70),
    "maison": (20, 300),
}

random.seed(42)  # même résultat à chaque exécution
os.makedirs("data", exist_ok=True)

produits = []
id_produit = 1

for categorie in sorted(os.listdir(DOSSIER_IMAGES)):
    chemin_categorie = os.path.join(DOSSIER_IMAGES, categorie)
    if not os.path.isdir(chemin_categorie):
        continue

    prix_min, prix_max = PRIX.get(categorie, (10, 200))

    for numero, fichier in enumerate(sorted(os.listdir(chemin_categorie)), start=1):
        if not fichier.lower().endswith(EXTENSIONS):
            continue

        produits.append({
            "id": id_produit,
            "nom": f"{categorie.capitalize()} {numero}",
            "categorie": categorie,
            "prix": random.randint(prix_min, prix_max),
            "image_path": f"images/{categorie}/{fichier}",
        })
        id_produit += 1

with open(FICHIER_CSV, "w", newline="", encoding="utf-8") as f:
    colonnes = ["id", "nom", "categorie", "prix", "image_path"]
    writer = csv.DictWriter(f, fieldnames=colonnes)
    writer.writeheader()
    writer.writerows(produits)

print(f"{len(produits)} produits écrits dans {FICHIER_CSV}")