# Wordle Bot: A Data-Driven Approach to Old English Version of Wordle
## Goal
The objective of this project is to create an intelligent Wordle bot that leverages information theory and computational techniques to guide players towards the optimal word guess. The bot will analyze potential word choices, calculate their corresponding entropy, and play the best move possible. 

## Project Plan
1. Word Dictionary Compilation
Assemble a comprehensive word dictionary using the enchant and nltk libraries, resulting in a dataset of 4,997 words. The selection is based on qualitative linguistic analysis, ensuring a broad yet relevant word pool for gameplay. Even though these datasets included the names of citys and countrys too, I decided that it might be for the best to include some proper nouns and adjust my program accordingly.
2. Entropy Calculation and Word Recommendation
Entropy Analysis: For each potential word guess, calculate its entropy—a measure of uncertainty reduction, which reflects how well a word can narrow down the possible answers. The initial dataset will be analyzed to determine the word with the highest entropy.
Word Frequency Sorting: The highest entropy word options will be further sorted by word frequency, prioritizing common words that are more likely to appear in the game.
Recommendation: The bot will then suggest the word with the optimal balance of high entropy and word frequency, providing the player with the best possible move.
3. Output Generation
Solution Display: The bot will return a list of the top recommended solutions, each with its corresponding entropy value, allowing the user to make an informed decision.
Niche Words: The bot may also suggest niche words that, while less common, could provide a significant strategic advantage based on the entropy calculations.
4. Iterative Testing and Results Reporting
The bot will run through 50 rounds of Wordle, iterating its strategy with each round. The results, including the performance of each guess and its impact on narrowing down the possible answers, will be reported in a JSON format for further analysis.

## Methodology
### Information Theory: A Deeper Dive
Information theory, at its core, deals with the quantification of information. In the context of Wordle, entropy serves as a key metric for gauging the effectiveness of a word in reducing the pool of possible answers.

To conduct each of our calculations, we will utilize the concept of entropy. In Wordle, this can be interpreted as the probability distribution over all possible feedback patterns the game might return for a given word guess.
By calculating the entropy for each word, we identify the word that maximizes uncertainty reduction, effectively slicing the search space of potential answers in the most efficient manner.
For example, if a word has an entropy of 2, it reduces the possible answers by a factor of 4. A word with an entropy of 4 would reduce the answer set by 16.
The goal is to find the word that maximizes this reduction, leading the player closer to the correct answer with each guess.

### Implementation Strategy
Combinatorial Analysis: The bot will evaluate all possible outcomes for each word guess, considering the 3^5 possible feedback combinations (corresponding to the three possible states for each of the five letters: correct, present but incorrect position, and absent).
Parallel Processing: Multithreading techniques will be employed to optimize the entropy calculations, ensuring the bot runs efficiently even with a large dataset.
UI/UX Enhancements: While the current version employs a simple UI, future iterations could incorporate advanced visualization tools like Qt Designer and hvPlot for a more user-friendly experience.

## Reflection
After running a simulation my program averaged a score of 4.12. Some improvements that could be made could include a feature that would prioritize entropy in the first few guesses of the game and prioritize popularity of the word items only in the latter half instead of ranking on an average of both entropy and usability rate. This project ultimately gave me insight into data visualization with python and introduced me to a different application of computing than what I'm typically used to. Although this type of project is heavily math based, utilizing math to not only calculate, but to deduce was a different but noteworthy experience.

## Tools and Libraries
NLTK: Natural language processing library used for linguistic analysis and dictionary compilation. <br>
Asyncio: Multithreading library for simultaneous processing. <br>
Matplotlib: Visualization library used for plotting entropy distributions and other relevant data. <br>
NumPy: Fundamental package for numerical computations. <br>
Seaborn: Data visualization library that provides a high-level interface for drawing attractive statistical graphics. <br>
Enchant: Spellchecking library used to assemble the word dictionary. <br>
Wordfreq: Library to obtain word frequency information, aiding in the prioritization of common words. <br>
