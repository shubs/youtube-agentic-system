---
description: "Audit YouTube complet : recherche concurrentielle → brainstorm titres → structure contenu → review packaging"
---

# YouTube Audit Complet — Orchestrateur Multi-Agents

Lance un workflow complet d'audit YouTube pour le sujet : **$ARGUMENTS**

## Contexte créateur (pré-chargé)

Avant de commencer, rappelle le contexte :
- **Créateur** : Shubham SHARMA (@shubham_sharma, 274k abonnés)
- **Niche** : IA, Automatisation, Productivité
- **Positionnement** : Vulgarisateur tech FR — pont entre tech complexe et gens normaux
- **Audience principale** : Le Curieux Pressé (50-60%) — veut comprendre SANS devenir expert
- **Émotions cibles** : Moins largué, Excité/Motivé, Autonome/Capable
- **Actions cibles** : Tester l'outil, Automatiser un process

---

## RÈGLES D'ORCHESTRATION

Tu es l'**orchestrateur**. Tu ne fais PAS le travail toi-même. Tu délègues chaque étape à un subagent spécialisé via l'outil `Task` avec `subagent_type: general-purpose`.

### Principes fondamentaux :
1. **Chaque étape = un subagent `Task`** avec un prompt dédié
2. **Chaque subagent DOIT lire** ses fichiers d'instructions (agent .md + bible + contexte)
3. **Chaque subagent DOIT sauvegarder** son output dans un fichier markdown
4. **Le subagent suivant DOIT lire** le fichier de l'étape précédente
5. **Validation utilisateur** via `AskUserQuestion` entre chaque étape
6. **Si l'utilisateur veut itérer**, relance le subagent avec les ajustements demandés
7. **Tout en français**, exigeant et honnête

### Dossier de sortie :
Crée le dossier `output/audit-$ARGUMENTS/` (remplace les espaces par des tirets) au tout début via l'outil `Bash` avec `mkdir -p`.

---

## ÉTAPE 0 : Recherche concurrentielle

Lance un subagent `Task` avec le prompt suivant :

```
Tu es un analyste de marché YouTube.

1. Lis les fichiers suivants pour tes instructions et ton contexte :
   - .claude/agents/niche-auditor.md (tes instructions détaillées)
   - .claude/youtube-strategy-bible.md (ta base de connaissances)
   - .claude/contexte-createur.md (le profil du créateur)

2. Fais un audit du sujet "$ARGUMENTS" sur YouTube FR et EN :
   - Recherche les top vidéos existantes (utilise WebSearch pour chercher sur YouTube)
   - Analyse les patterns de titres et thumbnails
   - Identifie les gaps et opportunités
   - Estime le TAM (Total Addressable Market)

3. Sauvegarde ton analyse complète dans output/audit-$ARGUMENTS/00-recherche.md
   Utilise l'outil Write pour créer le fichier.

4. Termine en résumant les 3 insights principaux.

Tout en français.
```

**Après le subagent :** Lis `output/audit-$ARGUMENTS/00-recherche.md` et présente un résumé des insights à l'utilisateur.

**⏸️ AskUserQuestion** avec les options :
- "Continuer vers le brainstorm titres" (Recommended)
- "Approfondir la recherche"
- "Modifier le focus"

Si l'utilisateur veut itérer, relance le subagent avec les ajustements. Sinon, passe à l'étape 1.

---

## ÉTAPE 1 : Brainstorm titres

Lance un subagent `Task` avec le prompt suivant :

```
Tu es un expert en packaging YouTube.

1. Lis les fichiers suivants :
   - .claude/agents/title-ideator.md (tes instructions détaillées)
   - .claude/youtube-strategy-bible.md (ta base de connaissances)
   - .claude/contexte-createur.md (le profil du créateur)
   - output/audit-$ARGUMENTS/00-recherche.md (la recherche concurrentielle)

2. En t'appuyant sur la recherche concurrentielle, génère 10+ titres
   pour "$ARGUMENTS" en utilisant les frameworks du title-ideator :
   curiosity gap, versus, liste incomplète, histoire incomplète,
   curiosité contre-intuitive, format template.

3. Pour les 3 meilleurs titres, propose 3 concepts de thumbnail
   complémentaires (pas redondants avec le titre).

4. Sauvegarde dans output/audit-$ARGUMENTS/01-titres.md
   Utilise l'outil Write pour créer le fichier.

Tout en français.
```

**Après le subagent :** Lis `output/audit-$ARGUMENTS/01-titres.md` et présente les 3 meilleurs titres à l'utilisateur.

**⏸️ AskUserQuestion** avec comme options les 3 meilleurs titres extraits du fichier + "Nouvelles variantes".

Si l'utilisateur veut itérer, relance le subagent en précisant les ajustements. Sinon, note le titre choisi et passe à l'étape 2.

---

## ÉTAPE 2 : Structure du contenu

Lance un subagent `Task` avec le prompt suivant :

```
Tu es un expert en storytelling YouTube.

1. Lis les fichiers suivants :
   - .claude/agents/content-structurer.md (tes instructions détaillées)
   - .claude/youtube-strategy-bible.md (ta base de connaissances)
   - .claude/contexte-createur.md (le profil du créateur)
   - output/audit-$ARGUMENTS/01-titres.md (le titre et thumbnail validés)

2. Structure le contenu pour le titre validé par l'utilisateur :
   - Cold open en 3 phases (7s confirm + 20s personal + 10s new loop)
   - Blocs Q&A avec open loops
   - Rehooks aux moments clés
   - Q&A tracker (toujours au moins une question ouverte)

3. Sauvegarde dans output/audit-$ARGUMENTS/02-structure.md
   Utilise l'outil Write pour créer le fichier.

Tout en français.
```

**Après le subagent :** Lis `output/audit-$ARGUMENTS/02-structure.md` et présente un résumé de la structure à l'utilisateur.

**⏸️ AskUserQuestion** avec les options :
- "Valider et passer à la review" (Recommended)
- "Modifier le cold open"
- "Modifier la structure"
- "Recommencer"

Si l'utilisateur veut itérer, relance le subagent avec les ajustements. Sinon, passe à l'étape 3.

---

## ÉTAPE 3 : Review du packaging

Lance un subagent `Task` avec le prompt suivant :

```
Tu es un reviewer exigeant du packaging YouTube.

1. Lis les fichiers suivants :
   - .claude/agents/packaging-reviewer.md (tes instructions détaillées)
   - .claude/youtube-strategy-bible.md (ta base de connaissances)
   - .claude/contexte-createur.md (le profil du créateur)
   - output/audit-$ARGUMENTS/01-titres.md (titres et thumbnails)
   - output/audit-$ARGUMENTS/02-structure.md (structure du contenu)

2. Évalue le packaging complet sur les 6 dimensions :
   - Curiosity gap (sur 10)
   - Complémentarité titre/thumbnail (sur 10)
   - Valeur en un coup d'œil (sur 10)
   - "Familier mais différent" (sur 10)
   - Les 30 premières secondes (sur 10)
   - Test du "scroll stop" (sur 10)

3. Donne un diagnostic honnête et des suggestions d'amélioration.
   Propose des variantes améliorées si un score est < 7/10.

4. Sauvegarde dans output/audit-$ARGUMENTS/03-review.md
   Utilise l'outil Write pour créer le fichier.

Tout en français. Sois direct et honnête.
```

**Après le subagent :** Lis `output/audit-$ARGUMENTS/03-review.md` et présente le diagnostic final à l'utilisateur.

---

## Instructions globales
- **Tout le contenu doit être en français**
- Sois exigeant et honnête dans chaque étape
- Le livrable final = un dossier `output/audit-$ARGUMENTS/` avec 4 fichiers markdown structurés et actionnables
- **RAPPEL : tu DOIS utiliser `AskUserQuestion` et attendre la validation entre chaque étape**
- Si un subagent échoue ou produit un résultat insuffisant, relance-le avec un prompt ajusté
