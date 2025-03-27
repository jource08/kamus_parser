from pdf2image import convert_from_path
import pytesseract
import pdfplumber
from .logger import setup_logger
from .text_utils import clean_text, split_columns

# Initialize logger
logger = setup_logger()

def extract_text(pdf_path, is_scanned=False):
    """
    Extract text from a two-column PDF while ignoring drop caps.

    Args:
        pdf_path (str): Path to the PDF file.
        is_scanned (bool): Whether the PDF is scanned or text-based.

    Returns:
        str: Extracted and cleaned text.
    """
    try:
        if is_scanned:
            return _extract_text_from_images(pdf_path)
        else:
            return _extract_text_from_pdf(pdf_path)
    except Exception as e:
        logger.error(f"Error extracting text from {pdf_path}: {e}")
        return ""

def _extract_text_from_images(pdf_path):
    """Extract text from scanned PDFs using OCR."""
    images = convert_from_path(pdf_path)
    text = [clean_text(pytesseract.image_to_string(img)) for img in images if pytesseract.image_to_string(img).strip()]
    return "\n".join(text)

def _extract_text_from_pdf(pdf_path):
    """Extract text from text-based PDFs with two-column handling."""
    with pdfplumber.open(pdf_path) as pdf:
        extracted_text = [split_columns(page) for page in pdf.pages]
    return "\n".join(extracted_text)
