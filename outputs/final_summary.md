# Final Experiment Summary

This file was generated automatically by `python -m scripts.run_final_pipeline`.

## Configuration

- `n = 40` voters
- `m = 6` candidates
- `alpha = 0.0, 0.1, ..., 1.0`
- `phi_2` trials: `20`
- distance-measure trials: `10`
- k-means restarts for distance measures: `10`

## Trend Summary

- `phi_2 approval`: mean rises from 0.571 at alpha=0.0 to 0.951 at alpha=1.0.
- `phi_2 ranking`: mean rises from 0.500 at alpha=0.0 to 0.881 at alpha=1.0.
- `phi_dH approval`: mean rises from 0.055 at alpha=0.0 to 0.715 at alpha=1.0.
- `phi_dS ranking`: mean rises from 0.125 at alpha=0.0 to 0.501 at alpha=1.0.

## Output Files

- `outputs/data/final_phi2_approval.csv`
- `outputs/data/final_phi2_ranking.csv`
- `outputs/data/final_phidh_approval.csv`
- `outputs/data/final_phids_ranking.csv`
- `outputs/figures/final_phi2_approval.png`
- `outputs/figures/final_phi2_ranking.png`
- `outputs/figures/final_phidh_approval.png`
- `outputs/figures/final_phids_ranking.png`