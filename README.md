# Exploratory Analysis of Wordle

An exploratory analysis of the popular word game Wordle in Python using Jupyter Notebooks, also featuring a Wordle solver. 

## Introduction

Wordle is a web-based word game created by Josh Wardle and recently purchased by the New York Times. The simple word-guessing game has over 300,000 people attemting to guess "today's wordle" each and every day. 

The game is simple. Players need to guess each day's mystery five-letter word, with six tries to get it correct. After guessing a word, the game highlights each of the letters in your guess green, yellow, or grey. Green means that the letter you guessed is both in the mystery word and is in the right position, yellow means that the guessed letter is in the mystery word but in the wrong position, and grey means that your guessed letter is not present in the mystery word. 

According to the thousands who post their wordle scores to twitter each day, the aim of the game is not only guessing the mystery word, but guessing it in the least amount of attempts. One of the best ways to guess the mystery word in the fewest number of attempts is to have a solid starter word. Some people choose random starter words each time, some swear by their own starter word, but this investigation will aim to find the best wordle starter word using programming.

## Finding the Best Starter Word
### Backtesting 
One of the challenges of identifying the best starter word is the lack of a standardized metric to "score" them.  In order to 

### Letter Frequency Strategy
### Vowel Strategy
### Brute Force Strategy

### Extension

## Results
From the results of the brute force strategy, the best wordle starter word was determined to be "TOEAS". Like you, I have never heard of this word before, but it refers to the "toea", a monetary unit of Papua New Guienea. Eliminates

Now while guessing TOEAS will eliminate the number of possible guesses by 95.72%, it will more than likely never be the actual mystery word, meaning that this strategy makes it nearly impossible to guess the worlde on your first attempt. Guessing WWWWW on the other hand, gives you the possibility of guessing 

## Creating a Solver

The Wordle solver drew inspiration from the methods used in finding the optimal starter word; it utilized the process of elimination. From the feedback t


Logic rules
- remove from list if word has grey letter
- remove from list if word goes not have green letter in correct place
- remove from list if word does not have yellow letter
- remove from list if word has yellow letter in same place

## Files

- **analysis.ipynb** Finding the best starter word
- **solver.py** Wordle solver
- **list.txt** Word list
- **answers.txt** Answers list
- **packages.txt** Python packages needed to run this project

## References
- Bakhtiari, B., 2022. A Frequency Analysis on Wordle. [online] Medium. Available at: <https://towardsdatascience.com/a-frequency-analysis-on-wordle-9c5778283363> [Accessed 10 July 2022].
- Cruise, B., 2022. Wordle Valid Words. [online] Kaggle.com. Available at: <https://www.kaggle.com/datasets/bcruise/wordle-valid-words> [Accessed 11 July 2022].
- Rickard, M., 2022. Wordle: What's the Best Starting Word?. [online] Matt-rickard.com. Available at: <https://matt-rickard.com/wordle-whats-the-best-starting-word> [Accessed 10 July 2022].
- Sanderson, G., 2022. Solving Wordle using information theory. [online] YouTube. Available at: <https://www.youtube.com/watch?v=v68zYyaEmEA> [Accessed 14 July 2022].
- Victor, D., 2022. Wordle Is a Love Story. The New York Times, [online] Available at: <https://www.nytimes.com/2022/01/03/technology/wordle-word-game-creator.html> [Accessed 14 July 2022].
