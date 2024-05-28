from lib.greet import *

def test_greet_returns_greeting():
    result = greet('Will')
    assert result == 'Hello Will'