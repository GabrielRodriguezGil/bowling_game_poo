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
    assert ScoreCard("123451234512345123X45").score_points(frame) == 61

    frame = ScoreCard("9-9-9-9-9-9-9-9-9-XXX").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[10]) == LAST_FRAME_LENGHT_STRIKE
    assert ScoreCard("9-9-9-9-9-9-9-9-9-XXX").score_points(frame) == 111

    frame = ScoreCard("8/549-XX5/53639/9/X").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[10]) == LAST_FRAME_LENGHT_STRIKE
    assert ScoreCard("8/549-XX5/53639/9/X").score_points(frame) == 149


@pytest.mark.all_numbers
def test_not_last_strike():
    frame = ScoreCard("X9-9-9-9-9-9-9-9-9-").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[1]) == STRIKE_FRAME_LENGHT
    assert ScoreCard("X9-9-9-9-9-9-9-9-9-").score_points(frame) == 100

    frame = ScoreCard("XX9-9-9-9-9-9-9-9-").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[1]) == STRIKE_FRAME_LENGHT
    assert len(frame[2]) == STRIKE_FRAME_LENGHT
    assert ScoreCard("XX9-9-9-9-9-9-9-9-").score_points(frame) == 120

    frame = ScoreCard("XXX9-9-9-9-9-9-9-").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert len(frame[1]) == STRIKE_FRAME_LENGHT
    assert len(frame[2]) == STRIKE_FRAME_LENGHT
    assert len(frame[3]) == STRIKE_FRAME_LENGHT
    assert ScoreCard("XXX9-9-9-9-9-9-9-").score_points(frame) == 141


@pytest.mark.all_numbers
def test_fouls():
    frame = ScoreCard("9-9-9-9-9-9-9-9-9-9-").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert frame == {
        1: "90",
        2: "90",
        3: "90",
        4: "90",
        5: "90",
        6: "90",
        7: "90",
        8: "90",
        9: "90",
        10: "90",
    }
    assert ScoreCard("9-9-9-9-9-9-9-9-9-9-").score_points(frame) == 90

    frame = ScoreCard("9-3561368153258-7181").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert ScoreCard("9-3561368153258-7181").score_points(frame) == 82


@pytest.mark.all_numbers
def test_spare_not_extra_roll():
    frame = ScoreCard("9-3/613/815/-/8-7/8-").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert ScoreCard("9-3/613/815/-/8-7/8-").score_points(frame) == 121


@pytest.mark.all_numbers
def test_spare_in_extra_roll():
    frame = ScoreCard("X5/X5/XX5/--5/X5/").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert ScoreCard("X5/X5/XX5/--5/X5/").score_points(frame) == 175


@pytest.mark.all_numbers
def test_all_strikes():
    frame = ScoreCard("XXXXXXXXXXXX").create_frames()
    assert len(frame) == FRAMES_LENGHT
    assert ScoreCard("XXXXXXXXXXXX").score_points(frame) == 300
