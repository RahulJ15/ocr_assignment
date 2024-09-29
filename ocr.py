import cv2
import easyocr
from PIL import Image
import io
import numpy as np
from langdetect import detect  

class ImageOCR:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image_data = None 

    def convert_to_jpeg(self):
        img = Image.open(self.image_path)
        # Convert PNGs and other formats to RGB mode if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
       
        jpeg_image_data = io.BytesIO()
        img.save(jpeg_image_data, format='JPEG')
        jpeg_image_data.seek(0)
        self.image_data = jpeg_image_data

    def perform_ocr(self):
        if self.image_data:
            img = Image.open(self.image_data)
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        else:
            img_cv = cv2.imread(self.image_path)
        
        # Initialize EasyOCR reader for both Hindi and English languages
        reader = easyocr.Reader(['hi', 'en'], gpu=True)
        result = reader.readtext(img_cv, detail=1)  
        
        extracted_text = []
        last_y = 0
        paragraph = []
        detected_languages = set()  # To store all detected languages

        for entry in result:
            bbox, text, _ = entry
            top_left_y = bbox[0][1]
            try:
                detected_language = detect(text)
                detected_languages.add(detected_language)  # Add language to the set
            except:
                detected_language = "unknown"
            
            if top_left_y - last_y > 40:  
                if paragraph:
                    extracted_text.append(" ".join(paragraph))
                paragraph = [text]
            else:
                paragraph.append(text)
            
            last_y = top_left_y
        if paragraph:
            extracted_text.append(" ".join(paragraph))
        language_info = ", ".join([lang.upper() for lang in detected_languages])
        final_text = "\n\n".join(extracted_text
        return f"Detected Languages: {language_info}\n\n{final_text}"
                                 
if __name__ == "__main__":
    image_path = 'path_to_your_image_file.png'  # Replace with the path to your image
    ocr = ImageOCR(image_path)
    ocr.convert_to_jpeg()  # Converts to JPEG in memory
    text = ocr.perform_ocr()
    print("Extracted Text:")
    print(text)
