
# Assignment: OCR and Document Search Web Application Prototype

This repository has two scripts: 
- `ocr.py`, which executes Optical Character Recognition (OCR) on images.
- `streamlit_script.py`, a web interface built with Streamlit for displaying OCR results.

The app is live and can be accessed here: **[Streamlit App](https://iit-ocr-rahuljiandani.streamlit.app/)**.

## Environment Setup

### Python Dependencies
1. Clone or download the repository.
2. Install required Python libraries via:

   ```bash
   pip install -r requirements.txt
   ```

### System Dependencies
For OCR, system libraries are essential. Add the following to a `packages.txt` file for Streamlit deployment or install them locally on Linux:

```
libgl1-mesa-glx
libsm6
libxext6
```


## Running the Application Locally

1. **OCR Script**: Run the OCR script as follows:

   ```bash
   python ocr.py <path_to_image>
   ```

2. **Streamlit App**: Start the Streamlit app with:

   ```bash
   streamlit run streamlit_script.py
   ```

The app will be available at `http://localhost:8501`.

## Deployment Process

To deploy on Streamlit:
1. Include both `requirements.txt` and `packages.txt`.
2. Deploy the repository to Streamlit Cloud.

The live version can be accessed here: **[Streamlit App](https://iit-ocr-rahuljiandani.streamlit.app/)**.

## Dependencies

The Python and system dependencies are listed in `requirements.txt` and `packages.txt`:

- **Python Packages**:
  ```
  easyocr
  langdetect
  numpy
  opencv-python
  pillow
  pytesseract
  streamlit
  ```

- **System Libraries**:
  ```
  libgl1-mesa-glx
  libsm6
  libxext6
  ```
