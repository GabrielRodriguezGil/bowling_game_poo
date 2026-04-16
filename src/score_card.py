class ScoreCard:
    def __init__(self, score_card):
        self.score_card = list(score_card.replace("-", "0"))
        self.score = 0
        self.last_roll = None
        self.strike = "X"
        self.spare = "/"

    def calculate_points(self):
        self.score = 0
        rolls = []
        frames = self.score_card
        for roll in frames:
            if roll == self.strike:
                rolls.append(10)
            elif roll == self.spare:
                rolls.append(10 - rolls[-1])
            else:
                rolls.append(int(roll))

        roll_index = 0

        for frame in range(10):
            if rolls[roll_index] == 10:
                self.score += 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
                roll_index += 1

            elif rolls[roll_index] + rolls[roll_index + 1] == 10:
                self.score += 10 + rolls[roll_index + 2]
                roll_index += 2

            else:
                self.score += rolls[roll_index] + rolls[roll_index + 1]
                roll_index += 2

        return self.score
