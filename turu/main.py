import pickle
import warnings
warnings.filterwarnings("ignore")


class TuRu:
    """
    Модель бинарного классификатора тувинского/русского языка на базе sklearn.MultinomialNB()
    : load_model - загрузка предворительно обученной модели model_file
    : text_preroccesor - предварительная обработка текста
    : get_turu - базовая функция для обработки текста text_in
    """
    def __init__(self, text_in='', model_file=''):
        self.text_in = text_in
        self.model_file = model_file

    def load_model(self)->set:
        "Загрузка модели"
        with open(self, 'rb') as f:
            vec, clf = pickle.load(f)
        return vec, clf

    def text_preroccesor(self)->str:
        "Функция отчистки текста"
        text = str(self).lower()
        tokens = [x for x in text.split() if x.isalpha()]
        return ' '.join(tokens)

    def get_turu(self, model_file, text_in)->object:
        """Обработка текста моделью"""
        try:
            vec, clf = TuRu.load_model(model_file)
            text = TuRu.text_preroccesor(text_in)
            text_transforme = vec.transform([text])
            scor = clf.predict(text_transforme)
    
            if scor[0] == 1:
                return {"type": 1, "lang": "тувинский язык"}
            else:
                return {"type": 0, "lang": "русский язык"}
        except Exception as e:
            return {"type": 3, "lang": e}
