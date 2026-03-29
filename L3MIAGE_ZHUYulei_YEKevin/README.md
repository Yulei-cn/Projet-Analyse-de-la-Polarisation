# Projet Analyse de la Polarisation

Base de code Python pour le projet de polarisation electorale en L3 Info, dans le cadre du cours de Fondements Mathematiques pour l'Aide a la Decision.

## Prerequis

- Python 3.11 recommande
- dependances Python listees dans `requirements.txt`

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Structure du depot

- `src/` : logique principale du projet
- `scripts/` : scripts pour lancer les experiences et le pipeline final
- `tests/` : tests unitaires
- `outputs/` : fichiers CSV, figures et resume automatique generes par les scripts
- `report/` : rapport final au format LaTeX et PDF
- `main.py` : petite demonstration de bout en bout

## Fonctions principales

Le projet contient notamment :

- une generation de profils `approval` et `ranking` avec un niveau de polarisation controlable
- le calcul des quantites paire a paire `d^{c_k,c_l}(p)`
- l'implementation de la mesure `phi_2`
- le calcul de `u1` pour les votes par approbation et les ordres totaux
- une approximation de `u2_tilde` par clustering a deux groupes
- les mesures `phi_dH` et `phi_dS`
- des scripts pour reproduire les experiences des questions 6 et 15

## Lancer une demonstration rapide

```bash
python main.py
```

Cette commande affiche quelques valeurs de test pour verifier que la generation et les mesures fonctionnent ensemble.

## Lancer les experiences separement

```bash
python -m scripts.run_phi2_experiments
python -m scripts.run_distance_experiments
```

## Lancer le pipeline final

```bash
python -m scripts.run_final_pipeline
```

Ce pipeline genere en une seule execution :

- les tableaux CSV finaux dans `outputs/data/`
- les figures finales dans `outputs/figures/`
- un resume automatique dans `outputs/final_summary.md`

## Lancer les tests

```bash
pytest
```

## Fichiers utiles pour le rendu

- `report/final_report.tex` : source LaTeX du rapport final
- `report/final_report.pdf` : version PDF du rapport
- `outputs/data/` : resultats numeriques exportes
- `outputs/figures/` : figures utilisees dans le rapport

## Remarque

Le depot contient tout le necessaire pour reproduire les experiences principales et regenerer les figures du rapport final.
