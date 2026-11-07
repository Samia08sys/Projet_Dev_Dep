# Semaine 3 : l'API, notes du binôme

> Deux questions, quelques phrases chacune. Répondez avec ce que vous avez observé, pas avec le cours.

## 1. Pourquoi l'API refuse-t-elle de démarrer sans `models/sentiment.joblib`, plutôt que de démarrer et de répondre 503 ?

L'API charge le modèle dès son démarrage. Si le fichier sentiment.joblib est absent, le chargement échoue et l'application ne peut pas fonctionner correctement. Il est donc préférable de détecter immédiatement le problème plutôt que de démarrer une API incapable de traiter les prédictions. Nous avons observé ce comportement en renommant le fichier : l'API a affiché une erreur FileNotFoundError et a refusé de démarrer.

## 2. Un texte vide est refusé deux fois : par Pydantic, puis par `predict()`. Est-ce redondant ?

Non, ce n'est pas totalement redondant. Pydantic vérifie les données reçues par l'API avant de les traiter. La fonction predict() effectue également une vérification pour protéger la logique de prédiction, même si elle est appelée depuis un autre endroit que l'API. Les deux contrôles permettent donc de sécuriser l'application à différents niveaux.