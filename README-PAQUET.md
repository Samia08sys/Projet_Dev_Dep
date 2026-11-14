# Changelog

Toutes les modifications notables de ce projet sont documentées dans ce fichier.

## [1.0.0] - 2026-11-14

### Ajouté
- Version initiale du paquet `sentiment-app`.
- Commande `sentiment` pour la ligne de commande.
- Commande `sentiment --json` pour une sortie au format JSON.
- Commande `sentiment --version` pour afficher la version.
- Modèle entraîné (Scikit-learn) embarqué dans la roue.
- Tests de vérification du paquet installé.

### Limites connues
- Le modèle est entraîné sur un jeu de démonstration.
- Les avis ironiques ou complexes peuvent être mal classifiés.
- Le score de confiance n'est pas une garantie absolue.