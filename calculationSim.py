import nltk
import math
import itertools

from wordfreq import word_frequency
from wordNav import returnList

nltk.download('words', quiet=True)

def findNextGuess(word_list):
    values = ['0', 'Y', 'G']
    combinations = list(itertools.product(values, repeat=5))

    entropy = 0
    wordFreq = 0
    maxEntropy = 0
    bestEntries = []

    if (len(word_list) == 1):
        # print("Your best choice is: " + word_list[0] + " because there is only one option!")
        return [(word_list[0], float(1), float(getWordFrequency(word_list[0])))]
    else:
        for i, word in enumerate(word_list):
            word = word.lower()
            for combination in combinations:
                probability = float(len(returnList(word, 
                                                word_list, 
                                                combination[0], 
                                                combination[1], 
                                                combination[2], 
                                                combination[3], 
                                                combination[4]))/len(word_list))
                if (probability != 0):
                    entropy += probability * math.log2(1/probability)
            wordFreq = getWordFrequency(word)
            if (entropy >= maxEntropy):
                # print("inserted "+str(entropy))
                # print("inserted [" + ' '.join(map(str, bestWords)) + "] " + str(len(bestWords)))
                if (word, entropy, float(wordFreq)) not in bestEntries:
                    bestEntries.append((word, entropy, float(wordFreq)))
                    bestEntries.sort(key=lambda x:x[1], reverse = True)
                    if (len(bestEntries) > 5):
                        bestEntries.pop(-1)
                    maxEntropy = bestEntries[-1][1]
            # print(str(i)+" "+word+" "+str(entropy)+" "+str(wordFreq))
            entropy = 0
        bestEntries.sort(key=lambda x:x[2], reverse = True)
        # print("Your best choices are:\n" + '\n'.join(map(str, bestEntries)))
        print("<------------------>")
        return bestEntries

def getWordFrequency(word):
    lan = "en"
    freq = word_frequency(word, lan)
    if freq:
        try:
            number = float(freq)
            decimal_str = "{:.15f}".format(number).rstrip('0').rstrip('.')
            return decimal_str
        except ValueError:
            return "Invalid input"
    else:
        return 0

