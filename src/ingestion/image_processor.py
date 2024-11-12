from PIL import Image
import io

class ImageProcessor:
    def process(self, image_path):
        with open(image_path, 'rb') as img_file:
            img = Image.open(io.BytesIO(img_file.read()))
            # Image processing logic can go here
            return img
