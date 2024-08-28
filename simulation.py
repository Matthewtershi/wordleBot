import asyncio
import nltk
import random
import enchant

from nltk.corpus import words
from wordNav import *
from calculationSim import *

nltk.download('words')

async def simRound():
    d = enchant.Dict("en_US")
    attempts = 0
    word_list = words.words()
    five_letter_words = [word for word in word_list if len(word) == 5 and d.check(word)]
    five_letter_words = list(map(str.lower, five_letter_words))
    targetWord = random.choice(five_letter_words).lower()
    gameState = True
    previousGuesses = []
    matching_words = five_letter_words

    while gameState:
        attempts += 1

        if attempts == 1:
            guess = "raise"
        elif attempts > 6:
            return targetWord, attempts
        else:
            guess = next((word for word, _, _ in findNextGuess(matching_words) if word not in previousGuesses), None)
            if guess is None:
                print("No valid guess found, breaking the loop.")
                break
        
        if guess in previousGuesses:
            attempts -= 1
            continue

        previousGuesses.append(guess)

        if guess == targetWord:
            gameState = False
            return guess, attempts
        else:
            feedback = evaluate_guess(guess, targetWord)
            matching_words = returnList(guess, five_letter_words, feedback[0], feedback[1], feedback[2], feedback[3], feedback[4])
            matching_words = [word for word in matching_words if word not in previousGuesses]
            findNextGuess(matching_words)

    return None, attempts  # Return None if the loop exits without guessing correctly

async def main():
    
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
        guess, attempts = await simRound()
        if guess is not None:
            print(f"You got {guess} in {attempts} tries!")
        else:
            print(f"Failed to guess the word within {attempts} tries.")
        sum += attempts
    print("avg: " + str(float(sum)/rounds))

# asyncio.run(main())

