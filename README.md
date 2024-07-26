Goal:

Make a simple wordle bot that can analyze a word and using fundamental 
information theory and programming skills and advise the player 
as to which move to make with a functioning and simple UI.

Plan:
Assemble word dictionary with qualitative analysis of enchant AND nltk libraries (length of 4997)
Calculate best entropy with inital dataset and recommend final answer to the user based on the predicted words of the highest entropy
Sort highest entropy options by word frequency
Return solutions and their corresponding entropy

How:
Calculate the entropy of each combination of what the wordle might respond with. Entropy is this value that can be resembled as the number of bits we cut our total possible answers/responses by. If the entropy of a word is 2, that means that word cuts down the possibilities of what the answer could be by 2^2 or 4. If a word has an entropy of 4, the word would cut down the possible answer count by 2^4 or 16. Essentially we parse through all 3^5 combinations of results that could come from us guessing a word and find the combination that will cut down our results the most. 

Tools:
1. Pyodide
2. NLTK
3. Pandas
Packages:
1. pip install nltk
2. pip install enchant
3. pip install wordfreq
4. pip install pandas
