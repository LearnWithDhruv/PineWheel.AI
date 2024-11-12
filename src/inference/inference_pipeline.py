from src.inference.query_processor import QueryProcessor
from src.inference.context_retriever import ContextRetriever
from src.inference.response_generator import ResponseGenerator

class InferencePipeline:
    def __init__(self):
        self.query_processor = QueryProcessor()
        self.context_retriever = ContextRetriever()
        self.response_generator = ResponseGenerator()

    def answer_query(self, query):
        processed_query = self.query_processor.process(query)
        context = self.context_retriever.retrieve(processed_query)
        response = self.response_generator.generate(context)
        return response
