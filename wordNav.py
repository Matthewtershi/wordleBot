# return a list of all possible target words given a guess word and the simulation results
def returnList(word, word_list, c0, c1, c2, c3, c4):
    criteria = [c0, c1, c2, c3, c4]
    
    def matches_criteria(candidate): # returns true if candidate matches word characteristics
        for i, criterion in enumerate(criteria):
            if criterion == '0':
                if word[i] in candidate and word[i] == candidate[i]:
                    return False
            elif criterion == 'Y':
                if word[i] not in candidate or word[i] == candidate[i]:
                    return False
            elif criterion == 'G':
                if word[i] != candidate[i]:
                    return False
        return True
    

    filtered_words = [w for w in word_list if matches_criteria(w)]
    # print("basin matches: "+ str(matches_criteria("basis")))
    # print("evaluate answer: " + ' '.join(x for x in evaluate_guess("basin", "basis"))) 
    # there is only one GGGG0 so when you look beyond that my code doesnt detect GGGGY and GGGGG

    # the current problem is that my eval answer is only looking for exactly 0 or Y not both
    #print([element for element in word_list if element.startswith("basi")])

    return filtered_words

def evaluate_guess(guess, target):
    result = ['0'] * 5
    target_letter_count = {letter: target.count(letter) for letter in set(target)}

    for i in range(5):
        if guess[i] == target[i]:
            result[i] = 'G'
            target_letter_count[guess[i]] -= 1

    for i in range(5):
        if result[i] == '0' and guess[i] in target and target_letter_count[guess[i]] > 0:
            result[i] = 'Y'
            target_letter_count[guess[i]] -= 1

    return result