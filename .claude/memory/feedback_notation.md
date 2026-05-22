---
name: feedback-notation
description: Book notation convention — RVs capitalised, realised values lowercase, mathcal for noise and normal
metadata:
  type: feedback
  machine: all
---

The book uses strict notation that must be matched in all notebooks:
- Random variables: uppercase ($Y$, $X$, $\mathcal{E}$)
- Realised values: lowercase ($y$, $x$, $\varepsilon_k$)
- Normal distribution: $\mathcal{N}$, not $N$
- Noise RV: $\mathcal{E}$, not $\varepsilon$
- Conditioning: $Y \mid X = x$ (uppercase RV, lowercase realised value)
- Model equation form: $Y = g(X; \boldsymbol{\beta}) + \mathcal{E}$, not $y_i = g(x_i; \beta) + \varepsilon_i$

**Why:** Book (Burridge & Tosh, CUP) uses this convention throughout; notebooks must be consistent with it.

**How to apply:** Check every key ideas cell and equation for capitalisation. Indexed forms like $y_i$, $x_i$ are only correct when referring to specific realisations, not the general model.
