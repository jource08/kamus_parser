from .utils.ocr import extract_text
from .utils.parser import parse_entry
import re
import csv
import os

def pdf_to_csv(pdf_path, output_csv="dictionary.csv", is_scanned=False):
    """Convert PDF dictionary to CSV."""
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
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
        writer = csv.DictWriter(csvfile, fieldnames=parsed_entries[0].keys())
        writer.writeheader()
        writer.writerows(parsed_entries)
    
    print(f"Exported {len(parsed_entries)} entries to {output_csv}")