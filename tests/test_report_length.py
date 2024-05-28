from lib.report_length import *

def test_report_length_returns_correct_length():
    result = report_length('Will')
    assert result == "This string was 4 characters long."

def test_report_length_empty_string():
    result = report_length('')
    assert result == "This string was 0 characters long."