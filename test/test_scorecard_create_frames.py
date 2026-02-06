import pytest

from src.score_card import ScoreCard

FRAMES_LENGHT = 10
LAST_FRAME_LENGHT_STRIKE = 3
STRIKE_FRAME_LENGHT = 1


@pytest.mark.all_numbers
def test_all_pins_number():
    frame = ScoreCard("12345123451234512345").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert ScoreCard("12345123451234512345").score_points(frame) == 60


@pytest.mark.all_numbers
def test_last_strike():
    frame = ScoreCard("123451234512345123X45").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[10]) == LAST_FRAME_LENGHT_STRIKE

    frame = ScoreCard("9-9-9-9-9-9-9-9-9-XXX").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[10]) == LAST_FRAME_LENGHT_STRIKE

    frame = ScoreCard("8/549-XX5/53639/9/X").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[10]) == LAST_FRAME_LENGHT_STRIKE


@pytest.mark.all_numbers
def test_not_last_strike():
    frame = ScoreCard("X9-9-9-9-9-9-9-9-9-").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[1]) == STRIKE_FRAME_LENGHT

    frame = ScoreCard("XX9-9-9-9-9-9-9-9-").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[1]) == STRIKE_FRAME_LENGHT
    assert len(frame[2]) == STRIKE_FRAME_LENGHT

    frame = ScoreCard("XXX9-9-9-9-9-9-9-").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[1]) == STRIKE_FRAME_LENGHT
    assert len(frame[2]) == STRIKE_FRAME_LENGHT
    assert len(frame[3]) == STRIKE_FRAME_LENGHT


@pytest.mark.all_numbers
def test_fouls():
    frame = ScoreCard("9-9-9-9-9-9-9-9-9-9-").create_frames()
    assert len(frame) == FRAMES_LENGHT

    frame = ScoreCard("9-3561368153258-7181").create_frames()
    assert len(frame) == FRAMES_LENGHT


@pytest.mark.all_numbers
def test_spare_not_extra_roll():
    frame = ScoreCard("9-3/613/815/-/8-7/8-").create_frames()
    assert len(frame) == FRAMES_LENGHT


@pytest.mark.all_numbers
def test_spare_in_extra_roll():
    frame = ScoreCard("X5/X5/XX5/--5/X5/").create_frames()
    assert len(frame) == FRAMES_LENGHT


@pytest.mark.all_numbers
def test_all_strikes():
    frame = ScoreCard("XXXXXXXXXXXX").create_frames()
    assert len(frame) == FRAMES_LENGHT
