# TUVALANG
Набор предобученых NLP-моделей для обработки тувинского языка.

**Состав:**

- __TuRu__- модель бинарного классификатора(LT) тувинского/русского языка
- __Tuva2vec__ - модель эмбеддингов тувинского языка

**Примеры:**

#### Пример модели TuRu
```
from turu import TuRu
model_file = 'turu_model.pkl'
text_in = u'Февраль 17-де, ай санаашкыны-биле Чаа чылга – Шагаа байырлалынга тураскаадып, Тыва Республиканың күрүне шаңналдарын тывыскан.'
turu = TuRu()
lang = turu.get_turu(text_in=text_in, model_file=model_file)

out: {"type": 1, "lang": "tuvan"}
```

