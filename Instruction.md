# Hybrid Medical Diagnosis - Instructions

## What this project is

- **Part A:** Random Forest trained on `data/Training.csv` / `data/Testing.csv`.
- **Part B:** Expert rules and advice in `knowledge/`.
- **UI:** Streamlit - `app.py` plus pages under `pages/`.

Model files (`models/*.pkl`) are **not** committed. They are created by training or by the Docker entrypoint on Hugging Face.

---

## Run locally

Open a terminal in the project folder (where `app.py` lives).

### 1. Optional: virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Train the model

Creates `models/random_forest_model.pkl`, `label_encoder.pkl`, `symptom_columns.pkl`.

```bash
python train_model.py
```

### 4. Start the app

```bash
streamlit run app.py
```

If `streamlit` is not on PATH:

```bash
python -m streamlit run app.py
```

Open the URL shown (usually `http://localhost:8501`).

**You need:** `data/Training.csv` and `data/Testing.csv`.

---

## Hugging Face Space

- **SDK:** Docker (see `Dockerfile`).
- **Config:** YAML at the top of `README.md` (Hugging Face reads that file for Space settings).
- **Startup:** `docker-entrypoint.sh` runs `python train_model.py` if `.pkl` files are missing, then starts Streamlit on `$PORT` (default 8501).

Push the repo to your Space, then open the Space URL in the browser. First boot may take longer while training runs.

**Docs:** [Spaces configuration](https://huggingface.co/docs/hub/spaces-config-reference)

---

## Useful paths

| Item | Location |
|------|----------|
| Entry | `app.py` |
| Pages | `pages/1_Dashboard.py`, `pages/2_Predict.py` |
| Train | `train_model.py` |
| Data | `data/Training.csv`, `data/Testing.csv` |
| Rules / advice | `knowledge/rules.py`, `knowledge/advice.py` |

---

## Disclaimer

Educational and decision-support use only. Not medical advice.
