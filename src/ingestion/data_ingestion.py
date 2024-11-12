from ingestion.text_parser import TextParser
from ingestion.image_processor import ImageProcessor

class DataIngestion:
    def __init__(self):
        self.text_parser = TextParser()
        self.image_processor = ImageProcessor()

    def ingest_data(self, raw_data):
        text_data = raw_data.get("text", "")
        image_data = raw_data.get("images", [])
        
        structured_text = self.text_parser.parse(text_data)
        processed_images = [self.image_processor.process(img) for img in image_data]
        
        return structured_text, processed_images
