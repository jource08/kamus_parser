from dotenv import load_dotenv
import os
from src.pdf_to_csv import pdf_to_csv

load_dotenv()

pdf_to_csv(
    pdf_path=os.getenv("INPUT_PDF"),
    output_csv=os.getenv("OUTPUT_CSV"),
    is_scanned=os.getenv("IS_SCANNED") == "True"
)
