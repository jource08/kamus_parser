import re

def parse_entry(entry_text):
    """Parse a dictionary entry into structured data."""
    entry = {
        "headword": "",
        "part_of_speech": "",
        "definition": "",
        "example": "",
        "translation": ""
    }
    
    # Headword and POS extraction
    headword_match = re.search(r"(\b\w+\b)\s*\((\w+\.?)\)", entry_text)
    if headword_match:
        entry["headword"] = headword_match.group(1)
        entry["part_of_speech"] = headword_match.group(2)
    
    # Definition extraction
    definition_match = re.search(r"(?<=:\s)(.*?)(?=Contoh:|$)", entry_text, re.DOTALL)
    if definition_match:
        entry["definition"] = definition_match.group(1).strip()
    
    # Example and translation
    example_match = re.search(r"Contoh:\s*['\"](.*?)['\"]\s*\[(.*?)\]", entry_text)
    if example_match:
        entry["example"] = example_match.group(1)
        entry["translation"] = example_match.group(2)
    
    return entry