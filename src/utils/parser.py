import re
from .text_utils import preprocess_text

def parse_entry(entry_text):
    """
    Parse a single dictionary entry.

    Args:
        entry_text (str): Text of a dictionary entry.

    Returns:
        dict: Parsed entry with headword, part of speech, definitions, and examples.
    """
    entry = {"headword": "", "part_of_speech": "", "definitions": [], "examples": []}

    # Extract headword and part of speech
    match = re.match(r"^(\d*\s*)?(?P<headword>[A-Za-z\s]+?)\s+(?P<pos>[a-z]+\.)?", entry_text)
    if match:
        entry["headword"] = match.group("headword").strip()
        entry["part_of_speech"] = match.group("pos") or ""

    # Split definitions and examples
    parts = re.split(r"[:;]", entry_text, maxsplit=1)
    if len(parts) > 1:
        entry["definitions"] = [parts[0].strip()]
        entry["examples"] = [parts[1].strip()]

    return entry if entry["headword"] else None  # Skip invalid entries

def parse_multiple_entries(text):
    """
    Parse multiple dictionary entries.

    Args:
        text (str): Raw text containing multiple dictionary entries.

    Returns:
        list: List of parsed entries.
    """
    return [parse_entry(entry) for entry in preprocess_text(text) if parse_entry(entry)]
