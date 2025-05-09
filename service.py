import bentoml
import torch
from bentoml.io import JSON, Text
from transformers import AutoModelForSequenceClassification, AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

svc = bentoml.Service("sentiment_classifier", runners=[])


@svc.api(input=Text(), output=JSON())
def classify(text: str) -> dict:
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    probabilities = torch.softmax(logits, dim=1).tolist()[0]
    predicted_class = int(torch.argmax(logits, dim=1).item())

    sentiment = "positive" if predicted_class == 1 else "negative"
    return {
        "text": text,
        "sentiment": sentiment,
        "confidence": {
            "negative": round(probabilities[0], 2),
            "positive": round(probabilities[1], 2)
        }
    }
