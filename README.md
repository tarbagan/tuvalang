# TUVALANG
Набор предобученых NLP-моделей для обработки тувинского языка.

## Состав:

- __TuRu__- модель бинарного классификатора тувинского/русского языка
- __Tuva2vec__ - модель эмбеддингов тувинского языка

## Примеры:

### Пример модели TuRu
```
from turu import TuRu
model_file = 'turu_model.pkl'
text_in = u'Февраль 17-де, ай санаашкыны-биле Чаа чылга – Шагаа байырлалынга тураскаадып, Тыва Республиканың күрүне шаңналдарын тывыскан.'
turu = TuRu()
lang = turu.get_turu(text_in=text_in, model_file=model_file)

out: {"type": 1, "lang": "tuvan"}
```
### Пример модели Tuva2vec
```
(w2v_model, "тыва", ["улус", "чоон"]
```
out:
![Alt-текст]([https://avatars1.githubusercontent.com/u/5384215?v=3&s=460](https://raw.githubusercontent.com/tarbagan/tuvalang/main/tuva2vec/tuv2vec.png)https://raw.githubusercontent.com/tarbagan/tuvalang/main/tuva2vec/tuv2vec.png "Tuva2vec")
