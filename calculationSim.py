import nltk
import math
import itertools
import wolframalpha

from wolframclient.language import WolframLanguageSession
from wolframclient.language import wl, wlexpr
from wordNav import returnList

nltk.download('words', quiet=True)
session = WolframLanguageSession()
client = wolframalpha.Client('TLA3W3-AH63PKG75L')
    
def getWordFrequency(word):
    query = f"word frequency of {word} in English"
    try:
        res = client.query(query)
        print(f"Querying: {query}")  # Debug print
        results = list(res.results)
        if not results:
            print(f"No results for word: {word}")
            return 0

        result = results[0].text
        print(f"Raw result: {result}")  # Debug print
        # Try to parse the frequency value from the result text
        frequency = float(result.split()[0])
    except (StopIteration, AttributeError, ValueError) as parse_error:
        print(f"Parse error for word '{word}': {parse_error.__class__.__name__} - {parse_error}")
        frequency = 0
    except Exception as api_error:
        print(f"API error for word '{word}': {api_error.__class__.__name__} - {api_error}")
        frequency = 0
    
    return frequency

def get_word_frequency(word):
    query = "word frequency data for '{word}'"
    try:
        res = client.query(query)
        print(f"Querying: {query}")  # Debug print
        
        # Print the raw result to debug
        # raw_xml = res.xml
        print(f"Raw XML: {res}")  # Debug print
        
        results = list(res.results)
        if not results:
            print(f"No results for word: {word}")
            return 0

        result = results[0].text
        print(f"Raw result: {result}")  # Debug print

        # Attempt to parse the frequency value from the result text
        frequency = None
        for line in result.split('\n'):
            if 'per million words' in line:
                frequency = float(line.split()[0]) / 1_000_000
                break
        
        if frequency is None:
            print(f"Could not find frequency for word: {word}")
            frequency = 0
    except (StopIteration, AttributeError, ValueError) as parse_error:
        print(f"Parse error for word '{word}': {parse_error.__class__.__name__} - {parse_error}")
        frequency = 0
    except Exception as api_error:
        print(f"API error for word '{word}': {api_error.__class__.__name__} - {api_error}")
        frequency = 0
    
    return frequency

def findNextGuess(word_list):
    values = ['0', 'Y', 'G']
    combinations = list(itertools.product(values, repeat=5))

    entropy = 0
    wordFreq = 0
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
                # IMPLEMENT SIGMOID CURVE WITH WORDFREQ TO STREAMLINE ENTROPY CALCULATION
            wordFreq = get_word_frequency(word)
            if (entropy > maxEntropy):
                # print("inserted "+str(entropy))
                # print("inserted [" + ' '.join(map(str, bestWords)) + "] " + str(len(bestWords)))
                bestEntries.append((word, entropy, wordFreq))
                bestEntries.sort(key=lambda x:x[1], reverse = True)
                if (len(bestEntries) > 5):
                    bestEntries.pop(-1)
                maxEntropy = bestEntries[-1][1]
            
                
            print(str(i)+" "+word+" "+str(entropy)+" "+str(wordFreq))
            entropy = 0
        print("Your best choices are:\n" + '\n'.join(map(str, bestEntries)))
        print("------------------")

