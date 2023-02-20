from turu import TuRu

model_file = r'turu_model.pkl'
text_in = u'Февраль 17-де, ай санаашкыны-биле Чаа чылга – Шагаа байырлалынга тураскаадып, Тыва Республиканың күрүне шаңналдарын тывыскан.'

turu = TuRu()
lang = turu.get_turu(text_in=text_in, model_file=model_file)
