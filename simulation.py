import pandas as pd
import numpy as np
import nltk
import random
import enchant

from nltk.corpus import words
from wordNav import *
from calculationSim import *

nltk.download('words')

def round():
    d = enchant.Dict("en_US")
    attempts = 0
    word_list = words.words()
    five_letter_words = [word for word in word_list if len(word) == 5 and d.check(word)]
    five_letter_words = list(map(str.lower, five_letter_words))
    targetWord = random.choice(five_letter_words).lower()
    gameState = True
    previousGuesses = []

    while gameState:
        attempts += 1

        if (attempts == 1):
            guess = "raise"
        else:
            guess = next(word for word, _, _ in findNextGuess(matching_words) if word not in previousGuesses)
        
        previousGuesses.append(guess)

        if guess in previousGuesses:
            attempts -= 1
            break

        if guess == targetWord:
            gameState = False
            return guess, attempts
        else:
            feedback = evaluate_guess(guess, targetWord)
            matching_words = returnList(guess, five_letter_words, feedback[0], feedback[1], feedback[2], feedback[3], feedback[4])
            # print(findNextGuess(matching_words))
            # for i in range (len(obj)):
            #     print(" --- " + obj[i][0])
        # print(previousGuesses)

sum = 0
print("Start Sim")
while True:
    userinput = input("Enter rounds: ")
    try:
        rounds = int(userinput)
        break
    except ValueError:
        print("That's not a valid number. Please try again.")
for i in range(rounds):
    guess, attempts = round()
    print(f"You got {guess} in {attempts} tries!")
    sum += attempts
print("avg: " + str(float(sum)/rounds))
