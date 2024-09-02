import my_guess_game.py
def test_check_guess_bingo():
    x = 75
    y = 75
    expected = "bingo"
    actual = check_guess(x, y)
    assert expected == actual

def test_check_guess_higher():
    x = 50
    y = 35
    expected = "guess higher"
    actual = check_guess(x, y)
    assert expected  == actual

def test_check_guess_lower():
    x = 50
    y = 75
    expected = "guess lower"
    actual = check_guess(x, y)
    assert actual == expected

def test_check_game_str():
    x = 50
    y = "fifty two"
    with pytest.raises(ValueError) as e:
        check_guess(x, y)

    assert str(e) == "guess is not numberic"

def test_check_game_range():
    x = 50
    y = 144
    with pytest.raises(ValueError) as e:
        check_guess(x, y)

    assert str(e) == "number out of range"

def test_check_game_negative():
    x = 50
    y = -50
    with pytest.raises(ValueError) as e:
        check_guess(x, y)
    assert str(e) == "number negative"
