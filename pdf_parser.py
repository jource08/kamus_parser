import pdfplumber
import re
from pdf2image import convert_from_path
import pytesseract

def extract_text(pdf_path, is_scanned=False):
    if is_scanned:
        images = convert_from_path(pdf_path)
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)
        return text
    else:
        with pdfplumber.open(pdf_path) as pdf:
            return "\n".join([page.extract_text() for page in pdf.pages])

def clean_text(text):
    text = re.sub(r'Page \d+', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def parse_entry(entry_text):
    entry = {
        "headword": "",
        "pos_abbr": "",
        "definition": "",
        "example": "",
        "translation": ""
    }
    
    # Extract headword and POS
    headword_match = re.search(r"(\b\w+\b)\s*\((\w+\.?)\)", entry_text)
    if headword_match:
        entry["headword"] = headword_match.group(1)
        entry["pos_abbr"] = headword_match.group(2)
    
    # Extract definition
    definition_match = re.search(r"(?<=:\s)(.*?)(?=(Contoh:|$))", entry_text, re.DOTALL)
    if definition_match:
        entry["definition"] = definition_match.group(1).strip()
    
    # Extract example and translation
    example_match = re.search(r'Contoh:\s*"(.*?)"\s*\[(.*?)\]', entry_text)
    if example_match:
        entry["example"] = example_match.group(1)
        entry["translation"] = example_match.group(2)
    
    return entry