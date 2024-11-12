import openai
from config.config import config

openai.api_key = config.LLM_API_KEY

class ResponseGenerator:
    def generate(self, context):
        response = openai.Completion.create(
            model=config.LLM_MODEL,
            prompt=f"Answer based on context: {context}",
            max_tokens=150
        )
        return response["choices"][0]["text"]
