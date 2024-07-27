import pandas as pd
import numpy as np
import nltk
import random
import enchant

from nltk.corpus import words
from wordNav import *
from calculationSim import *

nltk.download('words')
d = enchant.Dict("en_US")

def round():

    attempts = 0
    word_list = words.words()
    five_letter_words = [word for word in word_list if len(word) == 5 and d.check(word)]
    five_letter_words = list(map(str.lower, five_letter_words))
    targetWord = random.choice(five_letter_words).lower()
    targetWord = "urial"
    gameState = True
    previousGuesses = []
    print("--answer-- " + targetWord)

    while gameState:
        attempts += 1

        guess = "raise" if attempts == 1 else next(word for word in findNextGuess(matching_words) if word not in previousGuesses)
        guess = guess[0]
        print("aaaaaaaaaaaaaaaaaaaaaaaa Current Guess: " + str(guess))
        guess = str(guess)
        
        if guess in previousGuesses:
            attempts -= 1
            print("Repeated guess error " + guess)
            break

        if guess == targetWord:
            gameState = False
            print("The word was " + guess + " in " + str(attempts) + " attempts")
            return attempts
        else:
            feedback = evaluate_guess(guess, targetWord)
            # print(f"Feedback: {' '.join(feedback)}")
            matching_words = returnList(guess, five_letter_words, feedback[0], feedback[1], feedback[2], feedback[3], feedback[4])
            # print("matching_words length: " + str(len(matching_words))) 
            findNextGuess(matching_words)
        previousGuesses.append(guess)
    return attempts

print("Start Sim")
while True:
    userinput = input("Enter rounds: ")
    try:
        rounds = int(userinput)  # or int(user_input) if you only want integers
        break
    except ValueError:
        print("That's not a valid number. Please try again.")
for i in range(rounds):
    data = round()