# sentiment-app

Package Python permettant de prédire automatiquement le sentiment d'un avis client rédigé en français.

Le package utilise un modèle de Machine Learning entraîné avec Scikit-learn pour classer un texte dans une catégorie de sentiment et retourner un score de confiance.

## Fonctionnalités

- Classification automatique des avis en français.
- Prédiction du sentiment à partir d'un texte.
- Retour du label prédit et du score de confiance.
- Utilisation depuis un programme Python.
- Utilisation directement depuis la ligne de commande.
- Sortie au format JSON.

## Installation

Télécharger le fichier `.whl` depuis la release GitHub du projet, puis exécuter :

```bash
pip install sentiment_app-1.0.0-py3-none-any.whl
```

Cette installation ajoute également la commande `sentiment` au système.

## Utilisation en Python

```python
from sentiment_app import predict

resultat = predict("Le produit est excellent et la livraison était rapide.")

print(resultat)
```

Exemple de résultat :

```python
{
    "label": "positive",
    "score": 0.92
}
```

Le résultat contient :
- `label` : la classe de sentiment prédite.
- `score` : le score de confiance du modèle.

## Utilisation en ligne de commande

Pour analyser un avis :

```bash
sentiment "Le produit est excellent et la livraison était rapide."
```

Pour obtenir une réponse au format JSON :

```bash
sentiment --json "Le produit est excellent et la livraison était rapide."
```

Pour afficher la version installée :

```bash
sentiment --version
```

## Gestion des erreurs

Le package refuse les textes vides ou invalides en levant une exception `ValueError` en Python.

En ligne de commande, une erreur est affichée dans la sortie d'erreur et le programme retourne le code 2.

## Limites connues

- Le modèle est entraîné principalement sur des avis en français.
- Les résultats dépendent de la qualité et du contenu du texte fourni.
- Les expressions ironiques, ambiguës ou complexes peuvent entraîner des erreurs de classification.
- Le score de confiance ne garantit pas que la prédiction est correcte.
- Le modèle ne remplace pas une analyse humaine pour les décisions importantes.

## Technologies utilisées

- Python 3.11+
- Scikit-learn 1.5
- Joblib
- Setuptools
- Wheel

## Version

**Version actuelle : 1.0.0**

Voir [CHANGELOG.md](CHANGELOG.md) pour consulter l'historique des versions.