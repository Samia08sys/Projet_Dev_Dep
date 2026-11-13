# Semaine 4 : tests approfondis et qualité, notes du binôme

## 1. Couverture

- Avant (étape A) : **91 %**, lignes jamais exécutées : **6 lignes**.
- Ligne 49 dans `api/main.py` : aucun test ne vérifiait le retour 503 lorsque le modèle n'est pas chargé.
- Lignes 77 à 79 : aucun test ne vérifiait la gestion d'une erreur interne pendant la prédiction.
- Lignes 85 à 87 : le lancement direct de l'application n'était jamais exécuté sous pytest.
- Après (étape D) : **à compléter après les tests d'intégration** ; lignes exclues de la mesure : à préciser selon la configuration finale.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
|---|---|---|
| Jeu d'or vide : 0 avis sur 20 | `test_jeu_or_complet` | Ajouter 20 avis annotés dans `data/jeu_or.csv`. |
| Environnement virtuel non activé | `test_virtualenv_active` | Activer `.venv` avant pytest. |
| Gestion incorrecte des erreurs HTTP | Tests d'intégration T26 | Corriger la gestion des exceptions dans `api/main.py`. |
| Entrées composées uniquement d'espaces | Tests des limites T22-T23 | Ajouter un validateur dans `api/schemas.py`. |
| Modèle trop sûr de ses prédictions sur du texte inconnu | Tests T24-T25 | Ajouter le seuil d'abstention. |

## 3. Seuil d'abstention

- Deux ou trois points de la courbe (`python src/courbe_seuil.py`) : à compléter après exécution.
- Seuil retenu : à compléter (0,60 par défaut).
- Part des avis envoyés à un humain : à compléter.
- Justification : le modèle doit pouvoir s'abstenir lorsqu'il n'a pas suffisamment confiance dans sa prédiction. Cela évite de présenter une prédiction incertaine comme une réponse fiable.

## 4. Jeu d'or

- Bilan (`python src/bilan_jeu_or.py`) : justes à compléter, abstentions à compléter, erreurs franches déclarées à compléter.
- Ce que ces chiffres disent du modèle : le jeu d'or permet d'évaluer le modèle sur des avis rédigés indépendamment des données d'entraînement, notamment les négations, l'ironie et les avis difficiles.

## 5. Outils statiques

- Remarques au départ : **Ruff : 11 remarques ; Mypy : aucune erreur (Success: no issues found in 4 source files).**
- Parmi les défauts de la partie 2, combien Ruff et Mypy avaient-ils signalés ? Ruff avait signalé plusieurs problèmes de qualité et de gestion des exceptions. Mypy n'avait signalé aucun problème, car le retour de `predict()` était insuffisamment typé.
- Conclusion : les outils statiques détectent certains défauts avant l'exécution, mais ne remplacent pas les tests fonctionnels et d'intégration.