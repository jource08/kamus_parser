import csv
from .utils.ocr import extract_text
from .utils.parser import parse_multiple_entries

from tqdm import tqdm

def pdf_to_csv(pdf_path, output_csv="dictionary.csv", is_scanned=False):
    text = extract_text(pdf_path, is_scanned)
    processed_entries = parse_multiple_entries(text)

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['headword', 'part_of_speech', 'definitions', 'examples']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in tqdm(processed_entries, desc="Writing to CSV"):
            writer.writerow(entry)

    print(f"Exported {len(processed_entries)} entries to {output_csv}")
