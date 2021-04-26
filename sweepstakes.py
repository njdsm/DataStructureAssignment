from contestant import Contestant
import random

class Sweepstakes:
    def __init__(self):
        self.contestants = {}

    def add_contestant(self, fname, lname,):
        self.contestants[str(len(self.contestants) + 1)] = Contestant(fname, lname)

    def get_winner(self):
        selection = random.randrange(1, len(self.contestants) + 1)
        #print(selection)
        #print(len(self.contestants))
        winner = self.contestants[str(selection)]
        print(winner.first_name, winner.last_name)