import re

def preprocess_text(text):
    """
    Merge lines within the same entry until a double new line is encountered.

    Args:
        text (str): Raw text of a dictionary entry.

    Returns:
        list: List of preprocessed entries with new lines merged.
    """
    entries = text.split("\n\n")  # Split by double new lines
    processed_entries = []

    for entry in entries:
        lines = entry.split("\n")
        merged_lines = []
        current_line = ""

        for line in lines:
            line = line.strip()
            if not line:
                continue

            current_line += " " + line if current_line else line

        if current_line:
            processed_entries.append(current_line)

    return processed_entries

def parse_entry(entry_text):
    entry = {
        "headword": "",
        "part_of_speech": "",
        "definitions": [],
        "examples": []
    }

    # More flexible regex for headword & POS extraction
    headword_match = re.match(r"^(\d*\s*)?(?P<headword>[A-Za-z\s]+?)\s+(?P<pos>[a-z]+\.)?", entry_text)
    if headword_match:
        entry["headword"] = headword_match.group("headword").strip()
        entry["part_of_speech"] = headword_match.group("pos") or ""

    # Extract definitions/examples
    definition_parts = re.split(r"[:;]", entry_text, maxsplit=1)
    if len(definition_parts) > 1:
        entry["definitions"] = [definition_parts[0].strip()]
        entry["examples"] = [definition_parts[1].strip()]

    return entry

def parse_multiple_entries(text):
    """
    Parse multiple dictionary entries from a block of text.

    Args:
        text (str): Raw text containing multiple dictionary entries.

    Returns:
        list: List of parsed entries.
    """
    # Preprocess the text to merge lines within entries
    processed_entries = preprocess_text(text)

    # Parse each entry
    parsed_entries = []
    for entry in processed_entries:
        parsed = parse_entry(entry)
        if parsed["headword"]:  # Skip invalid entries
            parsed_entries.append(parsed)

    return parsed_entries