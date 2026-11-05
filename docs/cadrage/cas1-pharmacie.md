# Fiche de cadrage : Ordonnances incomplètes en pharmacie

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Développer un système permettant de détecter automatiquement les informations manquantes dans une ordonnance afin d'aider le pharmacien à vérifier sa complétude avant son traitement.

## Utilisateur final (obligatoire)

Le pharmacien est l'utilisateur final du système, car il doit contrôler les informations de l'ordonnance et prendre la décision finale concernant sa conformité.

## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

Les règles métier sont retenues car (b) chaque information détectée comme manquante peut être vérifiée directement par le pharmacien, et (c) les contrôles reposent sur des règles simples avec un faible coût par requête. De plus, (d) une erreur peut avoir des conséquences sur la sécurité du patient, ce qui rend indispensable une validation humaine.

## Données nécessaires et leur origine (obligatoire)

Le système nécessite des ordonnances numérisées ou saisies, les champs à contrôler et les règles définissant les informations obligatoires. Ces données devront provenir de documents autorisés et de référentiels réglementaires validés par des professionnels compétents.

## Métrique de succès et seuil d'acceptation (obligatoire)

La métrique principale sera le rappel de détection des informations manquantes, avec un seuil cible d'au moins 95 % sur un jeu de validation représentatif. Le système devra également limiter les fausses alertes afin de ne pas perturber inutilement le travail du pharmacien.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une information manquante non détectée peut entraîner une mauvaise prise en charge et présenter un risque pour le patient. Le pharmacien devra vérifier chaque ordonnance et confirmer toute anomalie avant de prendre une décision.

## Risques éthiques ou de confidentialité (obligatoire)

Les ordonnances contiennent des données personnelles et médicales sensibles qui doivent rester confidentielles. Leur traitement nécessite une autorisation, une protection des accès, une sécurisation du stockage et une anonymisation lorsque cela est possible.

## Approche écartée et pourquoi (facultatif)

Le machine learning est écarté dans un premier temps car les règles de vérification peuvent être définies explicitement et ne nécessitent pas obligatoirement un apprentissage à partir de données étiquetées. Un modèle génératif seul est également écarté car ses réponses peuvent être imprécises.