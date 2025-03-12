import pdfplumber
import re
import csv
from pdf2image import convert_from_path
import pytesseract

def extract_text(pdf_path, is_scanned=False):
    """Extract text from PDF (text-based or scanned)."""
    if is_scanned:
        images = convert_from_path(pdf_path)
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)
        return text
    else:
        with pdfplumber.open(pdf_path) as pdf:
            return "\n".join([page.extract_text() for page in pdf.pages])

def parse_entry(entry_text):
    """Parse a dictionary entry into structured data."""
    entry = {
        "headword": "",
        "part_of_speech": "",
        "definition": "",
        "example": "",
        "translation": ""
    }
    
    # Extract headword and part of speech (e.g., "Rantau (n.)")
    headword_match = re.search(r"(\b\w+\b)\s*\((\w+\.?)\)", entry_text)
    if headword_match:
        entry["headword"] = headword_match.group(1)
        entry["part_of_speech"] = headword_match.group(2)
    
    # Extract definition (text before "Contoh:")
    definition_match = re.search(r"(?<=:\s)(.*?)(?=Contoh:|$)", entry_text, re.DOTALL)
    if definition_match:
        entry["definition"] = definition_match.group(1).strip()
    
    # Extract example sentence and translation (e.g., "Contoh: '...' [ID: ...]")
    example_match = re.search(r"Contoh:\s*['\"](.*?)['\"]\s*\[(.*?)\]", entry_text)
    if example_match:
        entry["example"] = example_match.group(1)
        entry["translation"] = example_match.group(2)
    
    return entry

def pdf_to_csv(pdf_path, output_csv="dictionary.csv", is_scanned=False):
    """Convert PDF dictionary to CSV."""
    # Extract and clean text
    text = extract_text(pdf_path, is_scanned)
    entries = re.split(r'\n\d+\.\s', text)[1:]  # Split by entry numbers
    
    # Parse entries
    parsed_entries = []
    for entry in entries:
        parsed = parse_entry(entry)
        if parsed["headword"]:  # Skip invalid entries
            parsed_entries.append(parsed)
    
    # Write to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['headword', 'part_of_speech', 'definition', 'example', 'translation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(parsed_entries)
    
    print(f"Exported {len(parsed_entries)} entries to {output_csv}")

# Example usage
if __name__ == "__main__":
    pdf_to_csv(
        pdf_path="minang_sample.pdf",
        output_csv="minang_dictionary.csv",
        is_scanned=False  # Set to True for scanned PDFs
    )