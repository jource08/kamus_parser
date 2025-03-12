# Indonesian Dictionary Parser

Converts PDF dictionaries (Bahasa Indonesia ↔ Local Languages) to structured CSV.

## Usage
1. install requirements `pip install -r requirements.txt`
2. Create a Sample PDF
Create minang_sample.pdf with content like:
```
1. Rantau (n.): Daerah perantauan. Contoh: "Ia pergi rantau ke Jawa." [ID: Wilayah perantauan]
2. Makan (v.): Mengonsumsi makanan. Contoh: "Dia makan nasi." [ID: Memakan]
```
3. Place PDFs in `data/input_pdfs`
4. Run the Script
```bash
python src/pdf_to_csv.py
```
5. Find results in data/output_csvs