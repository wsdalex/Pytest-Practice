from lib.check_codeword import *

def test_codeword_return_for_correct_codeword():
    result = check_codeword('horse')
    assert result == "Correct! Come in."


def test_codeword_if_word_is_close():
    result = check_codeword('have')
    assert result == "Close, but nope."

def test_codeword_wrong_word():
    result = check_codeword('wrong')
    assert result == "WRONG!"