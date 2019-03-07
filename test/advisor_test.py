from app.robo_advisor import to_usd

def test_something():
    assert (2 + 2) == 5

def test_to_usd():
    assert to_usd(123456.8) == "$123,456.70"
