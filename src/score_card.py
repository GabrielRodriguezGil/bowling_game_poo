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
            elif score_card[position] != Scoring.STRIKE.value:
                self.frames[self.frame_number] = score_card[position : position + 2]
                position += 2
                self.frame_number += 1
            else:
                self.frames[self.frame_number] = score_card[position : position + 1]
                position += 1
                self.frame_number += 1
        return self.frames

    def score_points(self, frames):
        assert isinstance(frames, dict)
        self.score = 0
        frames_values = frames.values()
        last_roll = None
        for frame in frames_values:
            if "X" in frame:
                self.score += 10
                last_roll = "X"
            elif "/" in frame:
                if last_roll == "X" or "/":
                    self.score += int(frame[0]) + 10
                last_roll = "/"
            else:
                self.score += int(frame[0]) + int(frame[1])
        return self.score
