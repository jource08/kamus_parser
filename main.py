from database import initialize_database
from pdf_parser import extract_text, clean_text, parse_entry
from database_operations import insert_word
import re

def process_pdf(pdf_path, is_scanned=False):
    # Initialize database with basic data
    initialize_database()
    
    # Extract and clean text
    raw_text = extract_text(pdf_path, is_scanned)
    cleaned_text = clean_text(raw_text)
    
    # Split into entries (simple split by numbering)
    entries = re.split(r'\n\d+\.\s', cleaned_text)[1:]  # Skip first empty
    
    # Process each entry
    for entry_text in entries:
        parsed = parse_entry(entry_text)
        if parsed["headword"]:  # Skip invalid entries
            insert_word(parsed)

if __name__ == "__main__":
    process_pdf("minang_sample.pdf", is_scanned=False)