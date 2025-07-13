from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification
from transformers import pipeline


class Model:
    def __init__(self):
        self.model_name_or_path = "HooshvareLab/distilbert-fa-zwnj-base-ner"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)
        self.model = AutoModelForTokenClassification.from_pretrained(self.model_name_or_path)
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer)

    def nering(self, text):
        ner_results = self.nlp(text)
        return ner_results


obj = Model()
print(obj.nering("سلام اسم من امیرحسین"))
