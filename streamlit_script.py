import streamlit as st
from PIL import Image
import io
from ocr import ImageOCR 
from langdetect import detect
import re

st.title("Image OCR and Language Detection")

with st.sidebar:
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True, width=300)

if uploaded_file is not None:
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format=image.format)  
    img_byte_array.seek(0) 

    ocr = ImageOCR(img_byte_array)  
    ocr.convert_to_jpeg() 
    extracted_text = ocr.perform_ocr()
    search_keywords = st.text_input("Enter keywords to search within the extracted text:")

    if search_keywords:
        keywords = [keyword.strip() for keyword in search_keywords.split(',')]
        highlighted_text = extracted_text
        for keyword in keywords:
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            highlighted_text = pattern.sub(
                lambda match: f"<mark style='background-color: yellow;'>{match.group(0)}</mark>",
                highlighted_text
            )

        st.subheader("Extracted Text with Highlights:")
        st.markdown(
            f"<div style= padding: 10px;'>{highlighted_text}</div>",
            unsafe_allow_html=True
        )
    else:
        st.subheader("Extracted Text:")
        st.write(extracted_text)
else:
    st.write("Please upload an image file.")
