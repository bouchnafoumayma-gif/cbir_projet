import os
import re

DOSSIER_IMAGES = "static/images"

# Cherche les noms du genre : sac (1).jpg
modele = re.compile(r"^([a-z]+)\s*\((\d+)\)\.(jpg|jpeg|png)$", re.IGNORECASE)

for dossier, _, fichiers in os.walk(DOSSIER_IMAGES):
    for fichier in sorted(fichiers):
        resultat = modele.match(fichier)
        if not resultat:
            continue

        type_produit = resultat.group(1).lower()
        numero = int(resultat.group(2))
        extension = resultat.group(3).lower()

        nouveau_nom = f"{type_produit}_{numero:02d}.{extension}"
        ancien_chemin = os.path.join(dossier, fichier)
        nouveau_chemin = os.path.join(dossier, nouveau_nom)

        if os.path.exists(nouveau_chemin):
            print("Déjà existant, ignoré :", nouveau_nom)
            continue

        os.rename(ancien_chemin, nouveau_chemin)
        print(f"{fichier}  ->  {nouveau_nom}")