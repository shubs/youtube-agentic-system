---
description: "Audit YouTube complet : brainstorm titres → structure contenu → review packaging"
---

# YouTube Audit Complet

Lance un workflow complet d'audit YouTube pour le sujet : **$ARGUMENTS**

## Contexte créateur (pré-chargé)

Avant de commencer, rappelle le contexte :
- **Créateur** : Shubham SHARMA (@shubham_sharma, 274k abonnés)
- **Niche** : IA, Automatisation, Productivité
- **Positionnement** : Vulgarisateur tech FR — pont entre tech complexe et gens normaux
- **Audience principale** : Le Curieux Pressé (50-60%) — veut comprendre SANS devenir expert
- **Émotions cibles** : Moins largué, Excité/Motivé, Autonome/Capable
- **Actions cibles** : Tester l'outil, Automatiser un process

## RÈGLE CRITIQUE : Validation entre chaque étape

**Tu DOIS utiliser l'outil `AskUserQuestion` entre chaque étape pour obtenir la validation de l'utilisateur AVANT de passer à l'étape suivante.** Ne passe JAMAIS à l'étape suivante sans avoir reçu une réponse explicite de l'utilisateur.

## Workflow en 3 étapes

### Étape 1 : Brainstorm de titres
Agis comme le **title-ideator**. Pour le sujet "$ARGUMENTS" :
1. **Utilise le framework IEA du contexte créateur** — adapte-le au sujet spécifique
2. Génère au minimum 10 titres en utilisant les frameworks : curiosity gap, versus, liste incomplète, histoire incomplète, curiosité contre-intuitive, format template
3. **Cible principalement "Le Curieux Pressé"** — titres clairs, promesse de résultat rapide
4. Pour les 3 meilleurs titres, propose 3 concepts de thumbnail complémentaires (pas redondants avec le titre)

**⏸️ STOP — Utilise `AskUserQuestion` pour demander à l'utilisateur :**
- Quel(s) titre(s) il préfère parmi les propositions
- S'il veut des modifications ou de nouvelles variantes
- Si on peut passer à la structuration du contenu
- Propose les 3 meilleurs titres comme options + "Autre" pour qu'il puisse préciser

**ATTENDS la réponse avant de continuer. Si l'utilisateur demande des modifications, itère sur l'étape 1 jusqu'à ce qu'il valide.**

---

### Étape 2 : Structure du contenu
Agis comme le **content-structurer**. Pour le titre validé par l'utilisateur :
1. Conçois le cold open (7s confirm + 20s personal + 10s new loop)
2. Structure le contenu en blocs Q&A avec open loops
3. Identifie les moments de rehook
4. Assure-toi qu'il y a toujours au moins une question ouverte

**⏸️ STOP — Utilise `AskUserQuestion` pour demander à l'utilisateur :**
- Si la structure lui convient
- S'il veut modifier le cold open, les blocs ou les rehooks
- Si on peut passer à la review du packaging
- Propose des options : "Valider et passer à la review", "Modifier le cold open", "Modifier la structure", "Recommencer"

**ATTENDS la réponse avant de continuer. Si l'utilisateur demande des modifications, itère sur l'étape 2 jusqu'à ce qu'il valide.**

---

### Étape 3 : Review du packaging
Agis comme le **packaging-reviewer**. Évalue le packaging final :
1. Score le curiosity gap (sur 10)
2. Score la complémentarité titre/thumbnail (sur 10)
3. Score la valeur en un coup d'œil (sur 10)
4. Score le "familier mais différent" (sur 10)
5. Score les 30 premières secondes (sur 10)
6. Score le test du "scroll stop" (sur 10)
7. Donne un diagnostic et des suggestions d'amélioration

## Instructions
- Tout le contenu doit être **en français**
- Sois exigeant et honnête dans la review
- Propose des variantes améliorées si le score est inférieur à 7/10 sur un critère
- Le livrable final doit être un document actionnable prêt à l'emploi
- **RAPPEL : tu DOIS poser des questions et attendre la validation entre chaque étape**
