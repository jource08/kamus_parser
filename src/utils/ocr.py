from pdf2image import convert_from_path
import pytesseract
import pdfplumber

def extract_text(pdf_path, is_scanned=False):
    """Extract text from PDF (text-based or scanned)."""
    if is_scanned:
        images = convert_from_path(pdf_path)
        return "\n".join([pytesseract.image_to_string(img) for img in images])
    else:
        with pdfplumber.open(pdf_path) as pdf:
            return "\n".join([page.extract_text() for page in pdf.pages])