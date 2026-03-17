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

## Lancer les tests

```bash
pytest
```

## Etat actuel

Cette version fournit :

- un generateur de profils approval et ranking
- les distances de Hamming et de Spearman
- une premiere implementation de `phi_2`
- une premiere implementation de `u1`, `u2_tilde`, `phi_dH` et `phi_dS`
- des scripts d'experiences pour les questions 6 et 15

Certaines parties sont encore des approximations pragmatiques et devront etre alignees exactement avec les definitions finales du rapport.
