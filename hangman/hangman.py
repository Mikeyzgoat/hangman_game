import numpy as np
import random

# importing word list
import nltk
nltk.download('names')
from nltk.corpus import names
word_list = names.words()

# asking the user whether he will play again
def ask_user():
    case = input("Do you to play again? [y/n].")
    if(case == 'y'):
        hangman()
    else :
        quit()


# define the core of the game
def hangman():
    # creating array of words
    name = np.array(word_list)
    prompt = random.randint(0, 7943)
    # word declaration
    dis = name[prompt].lower()
    word_length = len(dis)
    word = list(dis)

    # add a global counter that counts number of guesses
    guess_count = 0
    chances = word_length - 1
    
    # game start
    print("The length of the word is",word_length,".")
    while(chances > 0) : 
        guess = input("make a guess : ").lower()
        if guess in word:
            guess_count = guess_count +1
            try:
                while True:
                    word.remove(guess)
            except ValueError:
                pass
            word_length = len(word)

            print("yippy!!, you made a right guess, now",word_length,"letter remain .")
        else :
            chances = chances -1
            guess_count = guess_count+1
            print("oops! ,you made a wrong guess, you have",chances,"chances remaining.")
    
    if(chances == 0):
        print("Unfortunately,You haven't guessed the word. The word was",dis,".")
        ask_user()
    else :
        print("woohoo!!, You got the word in",guess_count,"guesses. The word was",dis,".")
        ask_user()


# game starts
print("Welcome to Hangman!")
hangman()
