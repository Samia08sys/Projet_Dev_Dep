# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Développer un assistant intelligent capable de répondre aux questions des utilisateurs concernant le règlement intérieur en recherchant les informations pertinentes dans le document officiel.

## Utilisateur final (obligatoire)

Les étudiants, les enseignants et le personnel administratif sont les utilisateurs finaux de cet assistant, car ils peuvent avoir besoin de consulter rapidement les règles de fonctionnement de l'établissement.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

Le RAG est retenu car (a) il ne nécessite pas obligatoirement un dataset de questions-réponses étiquetées pour démarrer, mais utilise directement le règlement intérieur comme source documentaire, et (b) chaque réponse peut être vérifiée à partir des passages retrouvés dans le document. De plus, (d) une mauvaise interprétation d'une règle peut induire les utilisateurs en erreur, ce qui impose de fournir les sources utilisées.

## Données nécessaires et leur origine (obligatoire)

Le système nécessite le règlement intérieur officiel de l'établissement sous forme numérique, ainsi que ses différentes sections et articles. Le document devra être obtenu auprès de l'administration ou à partir d'une source institutionnelle autorisée et à jour.

## Métrique de succès et seuil d'acceptation (obligatoire)

La qualité sera évaluée avec le Recall@5 pour mesurer la capacité à retrouver les passages pertinents, avec un seuil cible d'au moins 90 %. Les réponses devront également être fidèles aux documents et comporter des références vérifiables.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une réponse incorrecte peut conduire un étudiant ou un membre du personnel à mal comprendre une règle de l'établissement. Les réponses importantes ou ambiguës devront être vérifiées auprès de l'administration ou d'un responsable compétent.

## Risques éthiques ou de confidentialité (obligatoire)

Le système doit utiliser uniquement des documents autorisés et à jour, sans divulguer des informations personnelles ou confidentielles. Il doit signaler lorsqu'une réponse ne peut pas être trouvée dans le règlement au lieu d'inventer une information.

## Approche écartée et pourquoi (facultatif)

Un modèle génératif seul est écarté car il peut produire des informations non présentes dans le règlement intérieur. Le RAG permet de fonder les réponses sur des passages documentaires vérifiables.