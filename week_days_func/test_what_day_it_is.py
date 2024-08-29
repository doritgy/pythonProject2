import what_day_it_is
import pytest
def test_what_day_numeric():
    x = "abc"
    with pytest.raises(ValueError) as e:
        what_day_it_is.what_day(x)
    assert str(e.value) == "day number not numeric"

def test_what_day_range():
    x = 8
    with pytest.raises(ValueError) as e:
        what_day_it_is.what_day(x)
    assert str(e.value) == "number out of range"