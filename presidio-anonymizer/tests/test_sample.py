import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    assert str(sample_run_anonymizer("My name is Bond.", 11, 15)) == "text: My name is BIP.\nitems:\n[\n    {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}\n]\n"