from src.pdf_to_csv import pdf_to_csv

if __name__ == "__main__":
    pdf_to_csv(
        pdf_path="data/input_pdfs/minang_sample.pdf",
        output_csv="data/output_csvs/minang_dictionary.csv",
        is_scanned=False
    )