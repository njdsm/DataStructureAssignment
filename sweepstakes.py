from contestant import Contestant
import random


class Sweepstakes:
    def __init__(self):
        self.contestants = {}

    def add_contestant(self, first_name, last_name,):
        self.contestants[str(len(self.contestants) + 1)] = Contestant(first_name, last_name)

    def get_winner(self):
        selection = random.randrange(1, len(self.contestants) + 1)
        winner = self.contestants[str(selection)]
        print(winner.first_name, winner.last_name)