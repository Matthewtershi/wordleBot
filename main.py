import nltk
import random
import enchant

from nltk.corpus import words
from wordNav import *
from calculationSim import *

nltk.download('words')
d = enchant.Dict("en_US")

attempts = 0
word_list = words.words()
five_letter_words = [word for word in word_list if len(word) == 5 and d.check(word)]
five_letter_words = list(map(str.lower, five_letter_words))
five_letter_words_count = len(five_letter_words)
targetWord = random.choice(five_letter_words).lower()
targetWord = "tidal"

print("Welcome to Wordle!")
print("------------------")
# findNextGuess(five_letter_words)
print("'raise' is the recommended best answer with 5.95 bits of expected information!")
while True:
    attempts += 1
    guess = input("Enter your guess (5-letter word): ").lower()
    if len(guess) != 5 or guess not in five_letter_words:
        print("Invalid input. Please enter a valid 5-letter word.")
        continue
        
    if guess == targetWord:
        print("Congratulations! You've guessed the word!")
        break
    else:
        feedback = evaluate_guess(guess, targetWord)
        print(f"Feedback: {' '.join(feedback)}")
        matching_words = returnList(guess, five_letter_words, feedback[0], feedback[1], feedback[2], feedback[3], feedback[4])
        findNextGuess(matching_words)
    print(targetWord)
print("------------------")
print("You solved this Wordle in " + str(attempts) + " tries!")