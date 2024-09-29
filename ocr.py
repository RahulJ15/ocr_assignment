import cv2
import easyocr
from PIL import Image
import io
import numpy as np

class ImageOCR:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image_data = None  # To store image data for in-memory processing

    def convert_to_jpeg(self):
        img = Image.open(self.image_path)
        # Convert PNGs and other formats to RGB mode if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Save the image as JPEG in memory
        jpeg_image_data = io.BytesIO()
        img.save(jpeg_image_data, format='JPEG')
        jpeg_image_data.seek(0)
        self.image_data = jpeg_image_data

    def perform_ocr(self):
        if self.image_data:
            # Load the image data from BytesIO for OCR processing
            img = Image.open(self.image_data)
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        else:
            img_cv = cv2.imread(self.image_path)
        
        # Initialize EasyOCR reader for both Hindi and English languages
        reader = easyocr.Reader(['hi', 'en'], gpu=True)  # Add 'hi' for Hindi
        result = reader.readtext(img_cv)
        extracted_text = " ".join([entry[1] for entry in result])
        return extracted_text

# Example usage (optional):
if __name__ == "__main__":
    image_path = 'path_to_your_image_file.png'  # Replace with the path to your image
    ocr = ImageOCR(image_path)
    ocr.convert_to_jpeg()  # Converts to JPEG in memory
    text = ocr.perform_ocr()
    print("Extracted Text:")
    print(text)
