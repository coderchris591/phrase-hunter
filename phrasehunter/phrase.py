# Create your Phrase class logic here.
class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f'{letter}', end=' ')
            elif letter not in guesses:
                print('_ ', end=' ')

    def check_guess(self, guess):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyz'
        if len(guess) != 1 or guess not in allowed_chars:
            print("\n\nWhoops, that's not a valid guess.")
        elif guess in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
