from statistics import mean

import torch
import requests

from service import model, tokenizer


texts = ["I love this!", "This is terrible.", "Awesome experience.", "Worst day ever."]
true_labels = [1, 0, 1, 0]

predictions = []
for text in texts:
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    predictions.append(int(torch.argmax(logits, dim=1).item()))

accuracy = mean((a == b) for a, b in zip(true_labels, predictions))
print(f"Accuracy before deployment: {accuracy}")

predicted_labels = []

for text in texts:
    response = requests.post("http://localhost:3000/classify", json={"text": text})
    result = response.json()
    predicted_labels.append(1 if result["sentiment"] == "positive" else 0)

accuracy = mean((a == b) for a, b in zip(true_labels, predictions))
print(f"Accuracy after deployment: {accuracy}")
