Goal:

Make a simple wordle bot that can analyze a word and using fundamental 
information theory and programming skills and advise the player 
as to which move to make with a functioning and simple UI.

Plan:
Calculate the entropy of each combination of what the wordle might respond with. Entropy is this value that can be resembled as the number of bits we cut our total possible answers/responses by. If the entropy of a word is 2, that means that word cuts down the possibilities of what the answer could be by 2^2 or 4. If a word has an entropy of 4, the word would cut down the possible answer count by 2^4 or 16. Essentially we parse through all 3^5 combinations of results that could come from us guessing a word and find the combination that will cut down our results the most. 

Packages:
1. pip install nltk
