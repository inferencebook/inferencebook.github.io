# Inference in Statistical Modelling and Machine Learning

Companion website for the textbook by James Burridge and Nick Tosh (Cambridge University Press).  
Live site: **[inferencebook.github.io](https://inferencebook.github.io)**

## Repository layout

```
index.html          — main page (served via GitHub Pages)
style.css           — site styles
notebooks/          — 14 Jupyter notebooks, one per chapter
data/               — CSV datasets used by the notebooks
src/                — utility scripts
*.pdf               — book PDF and solutions manuals
```

## Notebooks

Each notebook is linked from the site and opens directly in Google Colab.  They can also be run locally in Jupyter after cloning the repo — data files are loaded from `../data/` when not running in Colab.

| Chapter | Topic |
|---------|-------|
| 1  | Orientation |
| 2  | Supervised Learning Warm-Up |
| 3  | Unsupervised Learning Warm-Up |
| 4  | Probability, Likelihood and Bayes |
| 5  | Probabilistic Modelling |
| 6  | Frequentist and Bayesian Uncertainty |
| 7  | Frequentist Linear Regression |
| 8  | Directed Graphical Models |
| 9  | Bayesian Regression and Regularisation |
| 10 | Bayesian Methods |
| 11 | Classification |
| 12 | Unsupervised Learning |
| 13 | Neural Networks and Deep Learning |
| 14 | Expanding the Toolkit |

## Data files

| File | Used in | Description |
|------|---------|-------------|
| `bodyFatClean.csv` | Ch 7, 9 | Body fat measurements |
| `CP_birth_sequence.csv` | Ch 6 | Birth sequence data |
| `diabetes_data.csv` | Ch 11 | Diabetes diagnostic features |
| `HadSWEP_daily.csv` | Ch 10 | Met Office daily precipitation, South-West England, 1931–2026 |
| `July_rain.csv` | Ch 10 | Rainy days in last two weeks of July per year (≥ 5 mm), 1931–2025 |
| `queens_data.csv` | Ch 3, 12 | Queens dataset (training) |
| `queens_test_data.csv` | Ch 3, 12 | Queens dataset (test) |
| `treasure.csv` | Ch 2 | Treasure hunt dataset |
| `Vowels_Processed.csv` | Ch 12 | Vowel formant data |

## Running locally

```bash
git clone https://github.com/inferencebook/inferencebook.github.io.git
cd inferencebook.github.io
jupyter notebook notebooks/chapter_01_orientation.ipynb
```

No build step is needed for the site — GitHub Pages serves `index.html` directly.