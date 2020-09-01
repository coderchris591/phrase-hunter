import random
from phrasehunter.phrase import Phrase

class Game():

    def __init__(self):

        # Tracks the number of missed guesses by the player
        self.missed = 0

        # list of phrase objects to use with the game
        self.phrases = [
        Phrase('Come at me bro'),
        Phrase('as easy as pie'),
        Phrase('Epic Sax Guy'),
        Phrase('Hello world'),
        Phrase('One of a kind')
         ]

        # Phrase object that is currently in play
        self.active_phrase = self.get_random_phrase()

        # list that contains all the guesses made by the user during the course of the game
        self.guesses = [' ']

    def get_random_phrase(self):
        random_phrase = random.choice(self.phrases)
        return random_phrase


    def welcome(self):
        print('\n     ~~~~~~~~~~~~~~~~~~~~~~~~' )
        print("     Welcome to Phrase Hunter!")
        print("     ~~~~~~~~~~~~~~~~~~~~~~~~")


    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print('\nNumber missed:', self.missed)
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()
        self.play_again()


    def get_guess(self):
        guess = input('\n\nGuess a letter:  ')
        return guess


    def game_over(self):
        if self.missed == 5:
            print("\nGame Over!")
        else:
            print("\nCongratulations, You Won!!")

    def play_again(self):
        play = input('\nWould you like to play again? (y/n)  ')
        if play == 'y':
            self.__init__()
            self.start()
        elif play == 'n':
            print("Thanks for Playing! :)")
