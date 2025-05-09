# Sentiment Classifier API (BentoML)

## Установка

```bash
pip install -r requirements.txt
```

## Сборка и запуск сервиса

```bash
bentoml build
bentoml serve
```

## Тестирование

```bash
curl -X POST http://localhost:3000/classify -H "Content-Type: application/json" -d '{"text":"I love this product!"}'
```

## Метрики

http://localhost:3000/metrics
