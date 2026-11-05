# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Développer un système capable d'analyser les avis clients, de détecter les avis négatifs et de les identifier afin de faciliter leur traitement prioritaire par le service client.

## Utilisateur final (obligatoire)

Le responsable du service client et les équipes chargées de la gestion des réclamations sont les utilisateurs finaux, car ils doivent identifier rapidement les avis négatifs nécessitant une intervention.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

Le machine learning supervisé est retenu car (a) le fichier sample_reviews.csv contient déjà des avis étiquetés positive et negative, ce qui permet de constituer un premier jeu d'apprentissage, et (c) un modèle de classification comme TF-IDF associé à une régression logistique permet d'effectuer des prédictions avec un coût faible par requête. De plus, (b) chaque prédiction peut être vérifiée par un responsable du service client.

## Données nécessaires et leur origine (obligatoire)

Le projet dispose actuellement d'un fichier data/sample_reviews.csv contenant 10 avis clients, avec une colonne review pour le texte et une colonne label pour l'étiquette positive ou negative. Un jeu de données plus important et représentatif devra être collecté à partir d'avis clients autorisés afin d'améliorer la qualité du modèle.

## Métrique de succès et seuil d'acceptation (obligatoire)

La métrique principale sera le F1-score macro, avec un seuil cible d'au moins 0,80 sur un jeu de test indépendant et représentatif. La précision et le rappel de la classe negative seront également analysés pour limiter les avis négatifs non détectés.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un avis négatif mal classé peut ne pas recevoir de réponse rapide et nuire à la satisfaction du client. Un responsable devra pouvoir consulter les avis et corriger les classifications avant toute décision importante.

## Risques éthiques ou de confidentialité (obligatoire)

Les avis peuvent contenir des données personnelles, des propos sensibles ou des informations permettant d'identifier un client. Il faudra limiter les données collectées, anonymiser les informations personnelles et éviter toute discrimination liée au langage ou au profil des auteurs.

## Approche écartée et pourquoi (facultatif)

Les règles métier sont écartées car les expressions négatives peuvent varier selon le contexte et la formulation du client. Le machine learning permet d'apprendre des exemples étiquetés et de mieux généraliser à de nouveaux avis.