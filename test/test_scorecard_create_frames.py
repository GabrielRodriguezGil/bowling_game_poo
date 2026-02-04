import pytest

from src.score_card import ScoreCard

FRAMES_LENGHT = 10
LAST_FRAME_LENGHT_STRIKE = 3
STRIKE_FRAME_LENGHT = 1


@pytest.mark.all_numbers
def test_all_pins_number():
    assert len(ScoreCard("12345123451234512345").create_frames()) == FRAMES_LENGHT


@pytest.mark.all_numbers
def test_last_strike():
    frame = ScoreCard("123451234512345123X45").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[10]) == LAST_FRAME_LENGHT_STRIKE


@pytest.mark.all_numbers
def test_medium_strike():
    frame = ScoreCard("12X51234512345123X45").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[2]) == STRIKE_FRAME_LENGHT
