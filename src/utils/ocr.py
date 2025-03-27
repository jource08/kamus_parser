from pdf2image import convert_from_path
import pytesseract
import pdfplumber
from .logger import setup_logger  # Import logger

# Initialize logger
logger = setup_logger()

def extract_text(pdf_path, is_scanned=False):
    """Extract text from a two-column PDF (text-based or scanned)."""
    try:
        if is_scanned:
            # OCR-based approach (for scanned PDFs)
            images = convert_from_path(pdf_path)
            text = []
            for img in images:
                img_text = pytesseract.image_to_string(img)
                if img_text.strip():
                    text.append(img_text)
            return "\n".join(text)
        else:
            with pdfplumber.open(pdf_path) as pdf:
                extracted_text = []
                for page in pdf.pages:
                    width = page.width  # Get page width
                    height = page.height  # Get page height
                    
                    # Define left and right column bounding boxes
                    left_bbox = (0, 0, width / 2, height)  # Left column
                    right_bbox = (width / 2, 0, width, height)  # Right column

                    # Extract text from each column separately
                    left_text = page.within_bbox(left_bbox).extract_text() or ''
                    right_text = page.within_bbox(right_bbox).extract_text() or ''

                    # Combine left and right columns, ensuring correct order
                    page_text = left_text.strip() + "\n" + right_text.strip()
                    extracted_text.append(page_text)

                return "\n".join(extracted_text)
    except Exception as e:
        logger.error(f"Error extracting text from {pdf_path}: {e}")
        return ""
