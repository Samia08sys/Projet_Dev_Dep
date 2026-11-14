# Semaine 5 : Compte rendu de l'interface Streamlit (Membre B)

## 1. Pourquoi l'interface n'importe-t-elle jamais le modèle ?
L'interface web (Streamlit) agit uniquement comme un client HTTP. Elle ne charge jamais le fichier `.joblib` ni la fonction `predict()`. Elle envoie les avis de l'utilisateur à l'API via une requête `POST /predict`, et c'est l'API qui se charge d'appeler le modèle et de renvoyer la réponse. Cette séparation permet de réentraîner le modèle, de le mettre à jour ou de changer de serveur sans avoir à modifier une seule ligne de code de l'interface.

## 2. Que montre l'interface quand le modèle hésite (INDETERMINE) ?
Lorsque le score de confiance du modèle est inférieur au seuil d'abstention, l'interface affiche le verdict "Je ne sais pas : à faire vérifier par un humain", accompagné du pourcentage de confiance (ex: 52 %). Un encadré d'information précise que la confiance est trop basse. C'est beaucoup mieux qu'un verdict forcé : forcer un avis positif ou négatif sur un texte ambigu donnerait une fausse information à l'utilisateur, alors que l'abstention permet de passer la main à un humain.

## 3. Que voit l'utilisateur quand l'API tombe ?
Si l'API est arrêtée, l'interface ne plante pas. Dès qu'on recharge la page ou qu'on tente d'analyser un avis, l'interface affiche un message d'erreur rouge clair en haut de la page : "API injoignable : lancez d'abord uvicorn api.main:app". L'utilisateur comprend immédiatement que le problème vient du serveur et non de son texte.

## 4. Bilan des tests (T32 et T33)
- **T32 (Gestion des erreurs)** : La saisie de trois espaces déclenche bien le message d'avertissement "Texte refusé". L'arrêt de l'API déclenche bien l'erreur "API injoignable".
- **T33 (Fichier d'avis)** : Le chargement de `data/avis_exemple.csv` affiche correctement le tableau des 6 verdicts, le résumé des résultats et permet de télécharger le fichier CSV complété.