import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Verify text replacement
    assert "BIP" in result.text

    # Verify structure of the first item (use attributes instead of dict access)
    first_item = result.items[0]
    assert first_item.start == 11
    assert first_item.end == 14
    assert first_item.entity_type == "PERSON"
    assert first_item.text == "BIP"
    assert first_item.operator == "replace"