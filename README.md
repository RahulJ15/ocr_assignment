
# OCR and Streamlit App

This project includes two Python scripts: one for performing Optical Character Recognition (OCR) on images and the other for creating a simple user interface using Streamlit for specific functionalities.

## Table of Contents

- [OCR Script (`ocr.py`)](#ocr-script-ocrpy)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Example](#example)
- [Streamlit Script (`streamlit_script.py`)](#streamlit-script-streamlit_scriptpy)
  - [Installation](#installation-1)
  - [Usage](#usage-1)
  - [Running the Streamlit App](#running-the-streamlit-app)
- [Dependencies](#dependencies)

---

## OCR Script (`ocr.py`)

This script performs Optical Character Recognition (OCR) on input images, extracting text data and processing it for further use.

### Installation

1. Clone the repository or download the script.
2. Install the required dependencies:

```bash
pip install pytesseract pillow
```

Make sure you have [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) installed on your system. For example, on Ubuntu:

```bash
sudo apt install tesseract-ocr
```

On macOS, you can install it using Homebrew:

```bash
brew install tesseract
```

### Usage

You can use this script by passing an image file to it. For example:

```bash
python ocr.py <path_to_image>
```

### Example

```bash
python ocr.py ./sample_image.png
```

This will output the extracted text from the image.

---

## Streamlit Script (`streamlit_script.py`)

This script creates a simple user interface using Streamlit. The UI accepts inputs and displays the result of operations such as predictions or analysis.

### Installation

1. Install the required libraries:

```bash
pip install streamlit
```

### Usage

Run the Streamlit app using the following command:

```bash
streamlit run streamlit_script.py
```

### Running the Streamlit App

Once you run the above command, the Streamlit app will be available on `localhost:8501` by default. Open a web browser and navigate to `http://localhost:8501` to use the app.

---

## Dependencies

Both scripts depend on the following Python packages:

- `pytesseract` (for OCR functionality)
- `Pillow` (for image handling)
- `Streamlit` (for building the UI)

Make sure all dependencies are installed using the commands provided in the [Installation](#installation) sections above.

