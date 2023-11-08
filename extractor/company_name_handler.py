from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
import os

# Set a custom cache directory path in Colab


class modelInit:
    def __init__(self):

        custom_cache_dir = "./cache/models"
        os.makedirs(custom_cache_dir, exist_ok=True)

        # Specify the model name
        self.model_name = "xlm-roberta-large-finetuned-conll03-english"

        # Load the model and tokenizer
        model = AutoModelForTokenClassification.from_pretrained(
            self.model_name, cache_dir=custom_cache_dir)
        tokenizer = AutoTokenizer.from_pretrained(
            self.model_name, cache_dir=custom_cache_dir)

        # Initialize the token classification pipeline
        self.token_classifier = pipeline(
            "token-classification", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

    def extract(self, extracted_text):
        classifier = self.token_classifier(extracted_text)
        # Get the list of dictionary with key value pair "entity":'ORG'
        values = [item for item in classifier if item["entity_group"] == "ORG"]
        # Get the list of dictionary with key value pair "entity":'ORG'
        res = [sub['word'] for sub in values]
        final1 = list(set(res))  # Remove duplicates
        final = list(filter(None, final1))  # Remove empty strings
        return final
