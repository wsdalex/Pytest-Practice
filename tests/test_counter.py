from lib.counter import *

def test_count_is_zero():
    counter = Counter()
    assert counter.count == 0

def test_increasing_count():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5

def test_report():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

def test_multiple_adds():
    counter = Counter()
    counter.add(10)
    counter.add(10)
    assert counter.report() == "Counted to 20 so far."