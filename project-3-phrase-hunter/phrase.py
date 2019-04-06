class Phrase(object):
    """Class to handle creation and management of phrases."""
    def __init__(self, phrase):
        self._phrase = phrase
        self._guessed = set()
    
    """
    def check_letter(self, letter):
        if letter in self._guessed_letters:
            raise ValueError("This letter has already been guessed.")
        if letter in phrase:
            self._guessed_letters.append(letter)
            return True
        return False
    """

    def display(self):
        """Return the phrase with guessed letters revealed."""
        display_string = ""
        for letter in self._phrase:
            if letter in self._guessed:
                display_string += letter
            else:
                display_string += "_"

    def check_guess(self, letter):
        """Check if specified letter is in phrase."""
        if letter in self._phrase:
            self._guessed.add(letter)
            return True        

    def check_game(self):
        """Check if the entire phrase has been guessed."""
        return set(self._phrase) == self._guessed
