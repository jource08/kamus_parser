import os
import re
import csv
from .utils.ocr import extract_text
from .utils.parser import parse_entry

def pdf_to_csv(pdf_path, output_csv="dictionary.csv", is_scanned=False):
    """
    Convert a dictionary PDF to a structured CSV file.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_csv (str): Path to the output CSV file.
        is_scanned (bool): Whether the PDF is scanned (requires OCR).
    """
    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    # Extract text from the PDF
    text = extract_text(pdf_path, is_scanned)

    # Split text into individual entries
    entries = re.split(r'\n\d+\.\s', text)[1:]  # Skip the first empty part

    # Parse each entry
    parsed_entries = []
    for entry in entries:
        parsed = parse_entry(entry)
        if parsed["headword"]:  # Skip invalid entries
            parsed_entries.append(parsed)

    # Write parsed entries to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['headword', 'part_of_speech', 'definition', 'example', 'translation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(parsed_entries)

    print(f"Exported {len(parsed_entries)} entries to {output_csv}")