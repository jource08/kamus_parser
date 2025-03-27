from pdf2image import convert_from_path
import pytesseract
import pdfplumber
from .logger import setup_logger  # Import the logger setup function

# Initialize the logger
logger = setup_logger()

def extract_text(pdf_path, is_scanned=False):
    """Extract text from PDF (text-based or scanned)."""
    try:
        if is_scanned:
            images = convert_from_path(pdf_path)
            text = []
            for img in images:
                img_text = pytesseract.image_to_string(img)
                if img_text.strip():  # Avoid empty extractions
                    text.append(img_text)
            return "\n".join(text)
        else:
            with pdfplumber.open(pdf_path) as pdf:
                return "\n".join([page.extract_text() or '' for page in pdf.pages])
    except Exception as e:
        logger.error(f"Error extracting text from {pdf_path}: {e}")
        return ""
