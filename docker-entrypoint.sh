#!/bin/sh
set -e
cd /app

# Hugging Face / Docker: repo has no .pkl — train once when artifacts are missing.
if [ ! -f models/random_forest_model.pkl ] || \
   [ ! -f models/label_encoder.pkl ] || \
   [ ! -f models/symptom_columns.pkl ]; then
  echo "Model files missing — running python train_model.py ..."
  mkdir -p models
  python train_model.py
fi

exec streamlit run app.py --server.port="${PORT:-8501}" --server.address=0.0.0.0
