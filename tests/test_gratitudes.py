from lib.gratitudes import *

def test_add_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add('Being Happy')
    assert gratitudes.gratitudes == ['Being Happy']

def test_format_string():
    gratitudes = Gratitudes()
    gratitudes.add('Being Happy')
    gratitudes.add('Being Healthy')
    assert gratitudes.format() == "Be grateful for: Being Happy, Being Healthy"