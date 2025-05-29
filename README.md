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

## Верификация модели до и после деплоймента

```bash
python verificate_metrics.py
```

```shell
Accuracy before deployment: 1
Accuracy after deployment: 1
```

## Возможности BentoML

### Управление моделями

Можно хранить модели отдельно от сервиса. Это удобно, когда нужно переобучить модель, но логику API оставить той же.

### Контейнеризация

```shell
bentoml containerize my_bento
docker run -p 3000:3000 my_bento
```

Также можно разворачивать в k8s, в облаке и BentoCloud

### Поддержка асинхронности и параллелизма

```python
@bentoml.api(input_spec=JSON(), output_spec=JSON())
async def predict(self, input_data):
    result = await async_predict(input_data)
    return result
```

Можно настраивать количество рабочих процессов и потоков:

```shell
bentoml serve --workers=4
```

### Batch Inference

Объединение входящих запросов в батчи для повышения эффективности работы модели

```python
@bentoml.api(batchable=True)
def predict(self, inputs: list[InputType]):
    ...
```

### Управление ресурсами

Можно указать, сколько CPU/GPU использовать:

```yaml
# bentofile.yaml
services:
  - name: my_service
    resources:
      cpu: "2"
      gpu: "1"
```

или через код:

```python
@bentoml.service(gpu=1, workers=2)
class MyModelService:
    ...
```

### Управление зависимостями

Можно указать зависимости напрямую в `bentofile.yaml`:

```yaml
name: sentiment_classifier
build_config:
  python:
    packages:
      - torch
      - transformers
      - scikit-learn
```
