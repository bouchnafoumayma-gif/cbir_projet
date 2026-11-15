import os
import numpy as np
from feature_extractor import extraire_vecteur


def trouver(mot):
    """Retourne les chemins d'images dont le chemin contient le mot-clé."""
    resultats = []
    for dossier, _, fichiers in os.walk("static/images"):
        for f in fichiers:
            chemin = os.path.join(dossier, f)
            if mot in chemin.lower() and f.lower().endswith((".jpg", ".jpeg", ".png")):
                resultats.append(chemin)
    return sorted(resultats)


sacs = trouver("sac")
chaussures = trouver("chaussure")
lampes = trouver("lampe")

if len(sacs) < 2 or not chaussures or not lampes:
    print("Images introuvables. Sacs:", len(sacs),
          "Chaussures:", len(chaussures), "Lampes:", len(lampes))
    raise SystemExit

v_sac1 = extraire_vecteur(sacs[0])
v_sac2 = extraire_vecteur(sacs[1])
v_chaussure = extraire_vecteur(chaussures[0])
v_lampe = extraire_vecteur(lampes[0])

print("Forme du vecteur :", v_sac1.shape)
print("sac vs sac       :", round(float(np.dot(v_sac1, v_sac2)), 3))
print("sac vs chaussure :", round(float(np.dot(v_sac1, v_chaussure)), 3))
print("sac vs lampe     :", round(float(np.dot(v_sac1, v_lampe)), 3))