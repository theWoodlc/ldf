from calculator import add, sub, classify


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(5, 3) == 2


def test_classify():
    assert classify(1) == "positive"
    assert classify(-1) == "negative"
    assert classify(0) == "zero"
