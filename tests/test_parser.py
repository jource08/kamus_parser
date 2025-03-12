import pytest
from src.utils.parser import parse_entry

def test_parser():
    sample_entry = 'Rantau (n.): Daerah perantauan. Contoh: "Ia pergi rantau ke Jawa." [ID: Wilayah perantauan]'
    result = parse_entry(sample_entry)
    assert result["headword"] == "Rantau"
    assert result["part_of_speech"] == "n"
    assert "Daerah perantauan" in result["definition"]