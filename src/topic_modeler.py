import numpy as np
import torch

from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer

from __init__ import id2label, MODEL_DIR, BERT_FOLDER
from utils import download_model

download_model()
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_DIR / BERT_FOLDER)
trainer = Trainer(model, tokenizer=tokenizer)


def inference(text):
    encoding = tokenizer(text, return_tensors="pt",
                         padding="max_length", truncation=True, max_length=128)
    encoding = {k: v.to(trainer.model.device) for k, v in encoding.items()}
    outputs = trainer.model(**encoding)
    logits = outputs.logits
    sigmoid = torch.nn.Sigmoid()
    probs = sigmoid(logits.squeeze().cpu())
    predictions = np.zeros(probs.shape)
    predictions[np.where(probs >= 0.5)] = 1
    predicted_labels = [id2label[idx]
                        for idx, label in enumerate(predictions) if label == 1.0]
    return predicted_labels
