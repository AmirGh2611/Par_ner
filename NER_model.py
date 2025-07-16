from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification
from transformers import pipeline


class Model:
    def __init__(self):
        self.model_name_or_path = "HooshvareLab/distilbert-fa-zwnj-base-ner"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)
        self.model = AutoModelForTokenClassification.from_pretrained(self.model_name_or_path)
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer, aggregation_strategy="simple")

    def nering(self, text):
        ner_results = self.nlp(text)
        return ner_results

    @staticmethod
    def entity_expand(a):
        match a:
            case "DAT":
                return "Date"
            case "EVE":
                return "Event"
            case "FAC":
                return "Facility"
            case "LOC":
                return "Location"
            case "MON":
                return "Money"
            case "ORG":
                return "Organization"
            case "PCT":
                return "Percent"
            case "PER":
                return "Person"
            case "PRO":
                return "Product"
            case "TIM":
                return "Time"
        return None


obj = Model()
