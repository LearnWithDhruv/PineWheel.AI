from ingestion.data_ingestion import DataIngestion
from graph.graph_builder import GraphBuilder
from inference.inference_pipeline import InferencePipeline
from utils.logging_setup import setup_logging


logger = setup_logging()

def main():
    ingestion = DataIngestion()
    graph_builder = GraphBuilder()
    inference = InferencePipeline()
    
    # Example data
    raw_data = {"text": "Example scan result", "images": []}
    structured_text, processed_images = ingestion.ingest_data(raw_data)
    
    logger.info("Structured Text: %s", structured_text)
    logger.info("Processed Images: %s", processed_images)
    
    response = inference.answer_query("What ports are open on target.com?")
    logger.info("Response: %s", response)

if __name__ == "__main__":
    main()
