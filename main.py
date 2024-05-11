import random
from collections import Counter

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, num):
        if num >= len(self.contents):
            return self.contents.copy()

        balls_drawn = []
        for i in range(num):
            ball_index = random.randint(0, len(self.contents) - 1)
            balls_drawn.append(self.contents.pop(ball_index))

        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_count = Counter(expected_balls)
    successful_experiments = 0

    for i in range(num_experiments):
        hat_copy = hat.copy()
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls_count = Counter(balls_drawn)
        if all(balls_count[k] >= v for k, v in expected_count.items()):
            successful_experiments += 1

    return successful_experiments / num_experiments
