import string

class TextProcessor:
    def __init__(self):
        pass
    def get_clean_string(self, text):
        punctuation = string.punctuation
        no_punct = ""
        for char in text:
            if char not in punctuation:
                no_punct += char
        return no_punct
    def __is_punktiation(self, text):
        punctuation = string.punctuation
        punct = ""
        for char in text:
            if char in punctuation:
                punct += char
        if punct:
            return True
        else: return False

class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ''

    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)
        return self.__clean_string

    @property
    def clean_string(self):
         return f"Очищений текст {self.__clean_string}"

class Datainterfance:
    def __init__(self):
        self._text_loader = TextLoader()

    def process_texts(self, *args):
        clean_text = []
        for i in args:
            a = self._text_loader.set_clean_text(i)
            print(a)
            clean_text.append(a)

data = Datainterfance()
data.process_texts("dasda!!!$$sd", "dfsdfdfs")
