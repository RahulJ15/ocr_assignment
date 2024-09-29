import streamlit as st
from PIL import Image
import io
from ocr import ImageOCR  # Import the ImageOCR class from ocr.py
from langdetect import detect
import re

# Title of the app
st.title("Image OCR and Language Detection")

# Sidebar for uploading and displaying the image
with st.sidebar:
    # File uploader to upload an image
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image with reduced width to save screen space
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True, width=300)

# Check if a file is uploaded
if uploaded_file is not None:
    # Save the uploaded image to an in-memory file
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format=image.format)  # Keep the original format
    img_byte_array.seek(0)  # Reset buffer pointer

    # Initialize the OCR class with in-memory data and perform OCR
    ocr = ImageOCR(img_byte_array)  # Pass the in-memory byte array instead of a file path
    ocr.convert_to_jpeg()  # Convert to JPEG in memory if necessary
    extracted_text = ocr.perform_ocr()

    # Add a text input field for keyword search
    search_keywords = st.text_input("Enter keywords to search within the extracted text:")

    if search_keywords:
        # Split keywords into a list, handle multiple keywords separated by commas
        keywords = [keyword.strip() for keyword in search_keywords.split(',')]
        highlighted_text = extracted_text

        # Highlight keywords in the extracted text, case-insensitive
        for keyword in keywords:
            # Create a regex pattern for case-insensitive search
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)

            # Replace matches with highlighted version
            highlighted_text = pattern.sub(
                lambda match: f"<mark style='background-color: yellow;'>{match.group(0)}</mark>",
                highlighted_text
            )

        # Display highlighted text using Markdown with unsafe_allow_html
        st.subheader("Extracted Text with Highlights:")
        st.markdown(
            f"<div style= padding: 10px;'>{highlighted_text}</div>",
            unsafe_allow_html=True
        )
    else:
        # Display the extracted text without highlights
        st.subheader("Extracted Text:")
        st.write(extracted_text)

    # Detect and display the language of the extracted text
    if extracted_text:
        detected_language = detect(extracted_text)
        st.subheader("Detected Language:")
        st.write(detected_language)
else:
    st.write("Please upload an image file.")
