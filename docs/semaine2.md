\# Semaine 2 – Entraînement et évaluation du modèle de sentiment



\## 1. Objectif



L'objectif de cette deuxième semaine est de développer et d'évaluer un modèle de Machine Learning capable de classifier automatiquement les avis clients en deux catégories :

\- Positive

\- Negative



\## 2. Génération des données



Nous avons utilisé le script `src/make\_demo.py` pour générer un jeu de données de démonstration.



Résultats :

\- Nombre total d'avis : 290

\- Avis positifs : 145

\- Avis négatifs : 145

\- Présence d'avis mitigés et neutres pour tester la robustesse du modèle.



\## 3. Entraînement du modèle



L'entraînement a été réalisé avec :



```powershell

python src/train.py

```



Résultats obtenus :

\- Données d'entraînement : 232 avis

\- Données de test : 58 avis

\- Taille du vocabulaire : 316 termes

\- F1-score macro : 0.879



Le modèle dépasse le seuil minimum fixé à 0.85.



\## 4. Évaluation du modèle



L'évaluation a été réalisée avec :



```powershell

python src/evaluate.py

```



Résultats :

\- Accuracy : 0.879

\- Precision macro : 0.883

\- Recall macro : 0.879

\- F1-score macro : 0.879



\### Matrice de confusion



| Classe réelle | Negative | Positive |

|---|---:|---:|

| Negative | 27 | 2 |

| Positive | 5 | 24 |



Le modèle a effectué 7 erreurs sur les 58 avis de test.



\## 5. Expérimentation avec Allociné



Nous avons également testé le modèle sur le dataset Allociné avec :



```powershell

python src/train.py --allocine

```



Résultats :

\- Nombre d'avis : 20 000

\- Données d'entraînement : 16 000

\- Données de test : 4 000

\- Taille du vocabulaire : 149 529 termes

\- F1-score macro : 0.920



Cette expérimentation montre une amélioration des performances sur ce dataset.



\## 6. Tests automatisés



Les tests ont été exécutés avec :



```powershell

python -m pytest -q

```



Résultat final observé :

\- 41 tests réussis

\- 1 test échoué

\- 2 tests ignorés



Le test échoué concerne l'environnement virtuel Python (`test\_virtualenv\_active`).



Les tests liés aux métriques ont également nécessité la génération préalable du fichier `models/metrics.json`.



\## 7. Conclusion



Cette deuxième semaine a permis de mettre en place le pipeline d'entraînement et d'évaluation du modèle de classification des sentiments.



Le modèle atteint un F1-score macro de 0.879 sur les données de démonstration et de 0.920 sur le dataset Allociné.



Les prochaines étapes consistent à corriger le problème d'environnement virtuel, vérifier l'ensemble des tests et poursuivre l'intégration du modèle dans l'application.

