import os
import csv
import random

DOSSIER_IMAGES = "static/images"
FICHIER_CSV = "data/catalogue.csv"
EXTENSIONS = (".jpg", ".jpeg", ".png")

PRIX = {
    "mode": (15, 120),
    "electronique": (50, 900),
    "beaute": (8, 80),
    "jouets": (10, 70),
    "maison": (20, 300),
}

random.seed(42)
os.makedirs("data", exist_ok=True)

produits = []
id_produit = 1
compteur = {}  # pour numéroter chaque type : Sac 1, Sac 2...

# os.walk parcourt le dossier ET tous ses sous-dossiers
for dossier, _, fichiers in sorted(os.walk(DOSSIER_IMAGES)):
    chemin_relatif = os.path.relpath(dossier, DOSSIER_IMAGES)
    if chemin_relatif == ".":
        continue
    parties = chemin_relatif.split(os.sep)
    categorie = parties[0]

    for fichier in sorted(fichiers):
        if not fichier.lower().endswith(EXTENSIONS):
            continue

        # type du produit : nom du sous-dossier, sinon début du nom de fichier
        if len(parties) > 1:
            type_produit = parties[1]
        else:
            type_produit = fichier.split("_")[0]

        compteur[type_produit] = compteur.get(type_produit, 0) + 1
        prix_min, prix_max = PRIX.get(categorie, (10, 200))
        chemin_image = "/".join(parties + [fichier])

        produits.append({
            "id": id_produit,
            "nom": f"{type_produit.capitalize()} {compteur[type_produit]}",
            "categorie": categorie,
            "type": type_produit,
            "prix": random.randint(prix_min, prix_max),
            "image_path": f"images/{chemin_image}",
        })
        id_produit += 1

with open(FICHIER_CSV, "w", newline="", encoding="utf-8") as f:
    colonnes = ["id", "nom", "categorie", "type", "prix", "image_path"]
    writer = csv.DictWriter(f, fieldnames=colonnes)
    writer.writeheader()
    writer.writerows(produits)

print(f"{len(produits)} produits écrits dans {FICHIER_CSV}")
for type_produit, nombre in sorted(compteur.items()):
    print(f"  {type_produit} : {nombre}")