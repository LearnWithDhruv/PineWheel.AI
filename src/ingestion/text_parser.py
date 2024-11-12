import openai
from config.config import config

openai.api_key = config.LLM_API_KEY

class TextParser:
    def parse(self, text):
        response = openai.Completion.create(
            model=config.LLM_MODEL,
            prompt=f"Extract entities and relationships from the text: {text}",
            max_tokens=100
        )
        return response["choices"][0]["text"]
