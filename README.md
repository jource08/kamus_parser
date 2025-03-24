# Kamus Parser
A Python tool to parse dictionary PDFs (Bahasa Indonesia ↔ Local Languages) into structured CSV files.
---
## Features
- PDF Parsing: Extracts text from both text-based and scanned PDFs.
- CSV Export: Saves parsed dictionary entries into a CSV file.
- Flexible Structure: Handles headwords, parts of speech, definitions, examples, and translations.
---
## Installation
### Prerequisites
1. Python 3.9+: Download Python https://www.python.org/downloads/
2. Tesseract OCR: Install Tesseract https://github.com/tesseract-ocr/tesseract
### Steps
1. Install dependencies `pip install -r requirements.txt`
2. Setup directories `mkdir -p data/input_pdfs data/output_csvs`
---
### Usage
1. Add PDFs
    Place your dictionary PDFs in the data/input_pdfs folder.
2. Run the Script `python -m src.main`
3. Check Output. The parsed CSV will be saved in `data/output_csvs/minang_dictionary.csv`.
---
## File Structure
```
kamus_parser/
├── 📁 data/
│   ├── input_pdfs/          # Store PDFs here
│   └── output_csvs/         # Output CSV files
├── 📁 src/
│   ├── __init__.py
│   ├── main.py              # Main script
│   ├── pdf_to_csv.py        # PDF-to-CSV logic
│   └── 📁 utils/
│       ├── __init__.py
│       └── logger.py        # Logger
│       ├── ocr.py           # OCR functions
│       └── parser.py        # Parsing logic
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
---
```
## Example
### Input PDF (data/input_pdfs/minang_sample.pdf)
```
1. Rantau (n.): Daerah perantauan. Contoh: "Ia pergi rantau ke Jawa." [ID: Wilayah perantauan]
2. Makan (v.): Mengonsumsi makanan. Contoh: "Dia makan nasi." [ID: Memakan]
```
### Output CSV (data/output_csvs/minang_dictionary.csv)
``` csv
headword,part_of_speech,definition,example,translation
Rantau,n.,Daerah perantauan.,Ia pergi rantau ke Jawa.,Wilayah perantauan
Makan,v.,Mengonsumsi makanan.,Dia makan nasi.,Memakan
```
---
## Customization
1. Add New Fields. Edit src/utils/parser.py to extract additional fields (e.g., etymology, usage notes).

2. Handle Scanned PDFs. Set is_scanned=True in src/main.py:

``` python
pdf_to_csv(
    pdf_path="data/input_pdfs/minang_sample.pdf",
    output_csv="data/output_csvs/minang_dictionary.csv",
    is_scanned=True  # For scanned PDFs
)
```
---

## Troubleshooting
1. FileNotFoundError: [Errno 2] No such file or directory
Ensure the data/input_pdfs and data/output_csvs directories exist.

Use absolute paths if necessary.

2. ImportError: cannot import name 'extract_text'
Run the script from the project root:
```bash
python -m src.main
```
3. OCR Issues
Install Tesseract and ensure it’s in your system PATH.
For non-English languages, download the appropriate Tesseract language data.
---

## License
This project is licensed under the MIT License. See LICENSE for details.

---
## Acknowledgments
- pdfplumber for PDF text extraction.
- Tesseract OCR for scanned PDF support.