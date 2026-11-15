import sqlite3
import csv

FICHIER_DB = "data/catalogue.db"
FICHIER_CSV = "data/catalogue.csv"

# 1. Se connecter à la base (le fichier est créé s'il n'existe pas)
connexion = sqlite3.connect(FICHIER_DB)
curseur = connexion.cursor()


# 2. Créer la table (on repart de zéro à chaque exécution)
curseur.execute("DROP TABLE IF EXISTS produits")
curseur.execute("""
    CREATE TABLE produits (
        id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        categorie TEXT NOT NULL,
        prix REAL NOT NULL,
        image_path TEXT NOT NULL,
        vecteur BLOB
    )
""")

# 3. Lire le CSV et insérer chaque ligne dans la table
with open(FICHIER_CSV, newline="" , encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for linge in lecteur:
        curseur.execute(
            "INSERT INTO produits (id, nom, categorie, prix, image_path) "
            "VALUES (?, ?, ?, ?, ?)",
            (
                int(ligne["id"]),
                ligne["nom"],
                ligne["categorie"],
                float(ligne["prix"]),
                ligne["image_path"],
            ),
        )

# 4. Enregistrer les changements 
connexion.commit()

#5. Verifier
curseur.execute("SELECT COUNT(*) FROM produits")
print("Nombre de produits :",curseur.fetchone()[0])

curseur.execute("SELECT categorie, COUNT(*) FROM produits GROUP BY categorie")
for categorie, nombre in curseur.fetchall():
    print(f" {categorie} : {nomre}")

print("3 produit au hasard:")
curseur.execute("SELECT nom, prix FROM produits ORDER BY RANDOM() LIMIT 3")
for nom, prix in curseur.fetchall():
    print(f"  {nom} - {prix} MAD")


connexion.close()