import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    bond_test = sample_run_anonymizer("My name is Bond.", 11, 15)
    
    assert bond_test.text == "My name is BIP."
    assert len(bond_test.items) == 1
    assert bond_test.items[0].start == 11
    assert bond_test.items[0].end == 14