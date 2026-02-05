from src.scoring import Scoring


class ScoreCard:
    def __init__(self, score_card):
        self.score_card = score_card
        self.score = 0
        self.frame_number = 1
        self.frames = {}

    def create_frames(self):
        score_card = self.score_card
        position = 0
        while self.frame_number <= Scoring.TEN.value:
            if self.frame_number == Scoring.TEN.value:
                self.frames[self.frame_number] = score_card[position:]
                self.frame_number += 1
            elif score_card[position] != Scoring.SRIKE.value:
                self.frames[self.frame_number] = score_card[position : position + 2]
                position += 2
                self.frame_number += 1
            else:
                self.frames[self.frame_number] = score_card[position : position + 1]
                position += 1
                self.frame_number += 1
        return self.frames
