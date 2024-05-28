from lib.string_builder import *

def test_init_str():
    string_builder = StringBuilder()
    assert string_builder.str == ''

def test_add_str():
    string_builder = StringBuilder()
    string_builder.add('Hello World!')
    assert string_builder.str == 'Hello World!'

def test_size():
    string_builder = StringBuilder()
    string_builder.add('Hello')
    assert string_builder.size() == 5

def test_output():
    string_builder = StringBuilder()
    string_builder.add('Will')
    assert string_builder.output() == 'Will'