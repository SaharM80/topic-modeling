import os
from pathlib import Path

import gdown

from __init__ import MODEL_URL, MODEL_DIR, BERT_FOLDER


def download_model():
    if BERT_FOLDER not in os.listdir(MODEL_DIR):
        gdown.download_folder(MODEL_URL, output=str(
            MODEL_DIR / BERT_FOLDER), quiet=False)
