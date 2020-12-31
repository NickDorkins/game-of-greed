import pytest
from game_of_greed.game_logic import GameLogic

def test_length():
    logic = GameLogic()
    actual = len(logic.roll_dice(6))
    expected = 6
    assert actual == expected

def test_length2():
    logic = GameLogic()
    actual = len(logic.roll_dice(5))
    expected = 5
    assert actual == expected

def test_length3():
    logic = GameLogic()
    actual = len(logic.roll_dice(4))
    expected = 4
    assert actual == expected

def test_integer():
    logic = GameLogic()
    current_roll = logic.roll_dice(6)
    assert max(current_roll) < 7 and min(current_roll) > 0


