from enum import Enum, unique


@unique
class Scoring(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    SRIKE = "X"
    SPARE = "/"
    FOUL = "-"
