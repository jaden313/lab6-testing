import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
   
   result = sample_run_anonymizer("My name is Bond.", 11, 15)
   assert result.text == "My name is BIP."
   assert len(result.items) == 1
   first_item = result.items[0]
   assert first_item.start == 11
   assert first_item.end == 14
   first_item_dict = first_item.to_dict()
   assert first_item_dict["entity_type"] == "PERSON"
   assert first_item_dict["text"] == "BIP"
   assert first_item_dict["operator"] == "replace"