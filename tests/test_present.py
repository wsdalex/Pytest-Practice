from lib.present import *
import pytest

def test_wrap_sets_contents():
    present = Present()
    present.wrap('Teddy Bear')
    assert present.contents == 'Teddy Bear'

def test_unwrap_returns_contents():
    present = Present()
    present.wrap('Teddy Bear')
    assert present.unwrap() == 'Teddy Bear'

def test_error_if_contents_already_wrapped():
    present = Present()
    present.wrap('Teddy Bear')
    with pytest.raises(Exception) as e:
        present.wrap('Dollhouse')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_error_if_no_contents_has_been_wrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."