# Projet Analyse de la Polarisation

Base de code Python pour le projet de polarisation electorale.

## Structure

- `src/` : logique du projet
- `scripts/` : scripts pour lancer les experiences
- `tests/` : tests unitaires minimaux
- `outputs/` : fichiers csv et figures generes

## Installation

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

## Lancer un exemple rapide

```bash
python main.py
```

## Lancer les experiences

```bash
python -m scripts.run_phi2_experiments
python -m scripts.run_distance_experiments
```

## Lancer le pipeline final

```bash
python -m scripts.run_final_pipeline
```

Ce pipeline genere en une fois :

- les CSV finaux dans `outputs/data/`
- les figures finales dans `outputs/figures/`
- un resume automatique dans `outputs/final_summary.md`

## Lancer les tests

```bash
pytest
```

## Etat actuel

Cette version fournit :

- un generateur de profils approval et ranking
- les distances de Hamming et de Spearman
- une implementation corrigee de `phi_2`
- une implementation de `u1` pour approval et ranking
- une approximation de `u2_tilde` par clustering a deux groupes
- les mesures `phi_dH` et `phi_dS`
- des scripts d'experiences pour les questions 6 et 15
- trois rapports d'avancement dans `report/`
- une suite de tests unitaires

Le code est maintenant suffisant pour produire les graphes et les tableaux necessaires au rendu final.
Les principaux travaux restants concernent surtout la redaction theorique et la selection finale des resultats a commenter dans le rapport.
