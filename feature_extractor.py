"""Module d'extraction de caractéristiques (vecteurs) avec MobileNetV2."""

import numpy as np
from PIL import Image
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input



TAILLE_IMAGE = (224, 224)  # taille attendue par MobileNetV2

_modele = None  # le modèle sera chargé une seule fois


def charger_modele():
    """Charge MobileNetV2 sans la couche de classification (une seule fois)."""
    global _modele
    if _modele is None:
        _modele = MobileNetV2(
            weights="imagenet",
            include_top=False,
            pooling="avg",
        )
    return _modele


def preparer_image(source):
    """Ouvre une image et la prépare pour le modèle.

    source : chemin du fichier OU fichier ouvert (utile avec Flask).
    """
    image = Image.open(source).convert("RGB")    # 3 couleurs obligatoires
    image = image.resize(TAILLE_IMAGE)           # 224 x 224 pixels
    tableau = np.array(image, dtype=np.float32)  # image -> nombres
    tableau = np.expand_dims(tableau, axis=0)    # (224,224,3) -> (1,224,224,3)
    return preprocess_input(tableau)   # mise à l'échelle du modèle 


def extraire_vecteur(source):
    """Retourne le vecteur (1280 nombres) normalisé d'une image."""
    modele = charger_modele()
    image_preparee = preparer_image(source)
    vecteur = modele.predict(image_preparee, verbose=0)[0]

    # Normalisation : on ramène la "longueur" du vecteur à 1
    norme = np.linalg.norm(vecteur)
    if norme > 0:
        vecteur = vecteur / norme
    return vecteur