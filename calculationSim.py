import nltk
import math
import itertools

from nltk.corpus import words
from wordNav import returnList

nltk.download('words', quiet=True)
    
def findNextGuess(word_list):
    values = ['0', 'Y', 'G']
    combinations = list(itertools.product(values, repeat=5))

    entropy = 0
    maxEntropy = 0
    bestEntries = []

    if (len(word_list) == 1):
        print("Your best choice is: " + word_list[0] + " because there is only one option!")
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
            if (entropy > maxEntropy):
                print("inserted "+str(entropy))
                #print("inserted [" + ' '.join(map(str, bestWords)) + "] " + str(len(bestWords)))
                bestEntries.append((word, entropy))
                bestEntries.sort(key=lambda x:x[1], reverse = True)
                if (len(bestEntries) > 5):
                    bestEntries.pop(-1)
                maxEntropy = bestEntries[-1][1]
            
                
            print(str(i)+" "+word+" "+str(entropy))
            entropy = 0
        print("Your best choices are: " + ' '.join(map(str, bestEntries)))
        # print("Your best choices are: " + ' '.join(map(str, bestWords)))
        # print("With Entropys of: " + ' '.join(map(str, bestEntropy)))
        print("------------------")

