class ScoreCard:
    def __init__(self, score_card):
        self.score_card = score_card
        self.score = 0
        self.frame_number = 1
        self.frames = {}

    def create_frames(self):
        score_card = self.score_card
        position = 0
        while self.frame_number <= 10:
            if self.frame_number == 10:
                self.frames[self.frame_number] = score_card[position:]
                self.frame_number += 1
            elif score_card[position] != "X":
                self.frames[self.frame_number] = score_card[position : position + 2]
                position += 2
                self.frame_number += 1
            else:
                self.frames[self.frame_number] = score_card[position : position + 1]
                position += 1
                self.frame_number += 1
        return self.frames
