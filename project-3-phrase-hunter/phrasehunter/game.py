#premature optimization is the root of all evil
from random import choice
from phrasehunter.phrase import Phrase

class Game(object):
    """Class that contains methods for:
    starting the game,
    handling interactions,
    getting a random phrase,
    checking for a win/loss state,
    removing 'lives' from a player."""
    def __init__(self, phrases=["hello"]):
        self._phrases = phrases
        self._lives = 5
        self._gameover = False 

    def run(self):
        """Run the game until the player wins or exhausts lives."""
        phrase = Phrase(choice(self._phrases))
        phrase.display()
        while not self._gameover:
            guess = input("Guess a letter: ")
            if guess in phrase._guessed:
                print("You already guessed {}. Try another letter.".format(guess))
                continue
            if phrase.check_guess(guess):
                print("Correct guess!")
                phrase.display()
                if phrase.check_game():
                    self._gameover = True
                    print("You won! Game over.")
            else:
                print("Incorrect guess.")
                self._lives -= 1
                print("You have {} out of 5 lives remaining!".format(self._lives))
                if self._lives <= 0:
                    self._gameover = True
                    print("You have no more lives. Game over.")
