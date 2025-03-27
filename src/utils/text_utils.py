import re

def clean_text(text):
    """
    Remove uppercase single-letter drop caps.

    Args:
        text (str): Extracted text.

    Returns:
        str: Cleaned text without drop caps.
    """
    return re.sub(r'(?m)^[A-Z]$', '', text).strip()

def split_columns(page):
    """
    Extract and merge text from a two-column PDF page.

    Args:
        page (pdfplumber.page.Page): PDF page object.

    Returns:
        str: Merged text from left and right columns.
    """
    width, height = page.width, page.height
    left_text = (page.within_bbox((0, 0, width / 2, height)).extract_text() or '').strip()
    right_text = (page.within_bbox((width / 2, 0, width, height)).extract_text() or '').strip()
    return clean_text(f"{left_text}\n{right_text}")

def preprocess_text(text):
    """
    Merge lines within the same entry until a double new line is encountered.

    Args:
        text (str): Raw text of a dictionary entry.

    Returns:
        list: List of preprocessed entries with new lines merged.
    """
    entries = text.split("\n\n")  # Split by double new lines
    return [" ".join(line.strip() for line in entry.split("\n") if line.strip()) for entry in entries]
