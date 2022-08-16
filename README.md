# Exploratory Analysis of Wordle

An exploratory analysis of the popular word game Wordle in Python using Jupyter Notebooks, also featuring a Wordle solver. 

## Introduction

Wordle is a web-based word game created by Josh Wardle and was recently purchased by the New York Times. The simple word-guessing game has over 300,000 people attemting to guess "today's wordle" each and every day. 

The game is simple. Players need to guess each day's mystery five-letter word, with six tries to get it correct. After guessing a word, the game highlights each of the letters in your guess green, yellow, or grey. Green means that the letter you guessed is both in the mystery word and is in the right position, yellow means that the guessed letter is in the mystery word but in the wrong position, and grey means that your guessed letter is not present in the mystery word. 

According to the thousands who post their wordle scores to twitter each day, the aim of the game is not only guessing the mystery word, but guessing it in the least amount of attempts. One of the best ways to guess the mystery word in the fewest number of attempts is to have a solid starter word. Some people choose random starter words each time, some swear by their own starter word, but this investigation will aim to find the best wordle starter word using programming.

## Finding the Best Starter Word
### Backtesting 
One of the challenges in identifying the best starter word is the lack of a standardized metric to "score" them. In order to solve this, I created a back-testing function that would quantitatively evaluate each word based on how many words from the dataset it eliminated. This method of back-testing involved using the least informing wordle result; all letters highlighted grey, meaning that they are not present in the mystery word.If we optimized a word to eliminate a large number of possible words in spite of providing the least informing result, then that word would become an effective starter word. Therefore, this back-tester calculates the percentage of words eliminated from the dataset if a specific starter word is used.

<img width="582" alt="backtest" src="https://user-images.githubusercontent.com/80748482/184859772-a5368157-4450-4006-9370-8520f0134d53.png">

### Vowel Strategy
The first strategy considered was the vowel strategy. All English words (with some exceptions) have a vowel in them, and therefore eliminating the maximum number of vowels in a starter word should theorietically remove a maximum number of words from the dataset.

<img width="947" alt="vowelGraph" src="https://user-images.githubusercontent.com/80748482/184859808-9e4e0a97-237b-4a10-a6d0-0b0f64e689d7.png">


The vowels `a` and `e` were evidently more frequent that `i`, `o`, and `u`. In fact, having `e` in the starter word would immidiately eliminate over 50% of the words in the dataset.
The best words according to the vowel stratey were `aurei` and `uraei` which both eliminated 95.35% of all possibilities. 

<img width="392" alt="bestFreq" src="https://user-images.githubusercontent.com/80748482/184859780-00207977-b312-49ab-9b31-d4ce12bbc476.png">

### Letter Frequency Strategy
The letter frequency strategy was also attempted since while vowels were present in (almost) every single word, some consonants were more frequent. Therefore, eliminating those frequent consonants would result in a larger percentage of the dataset being eliminated.

<img width="937" alt="freqGraph" src="https://user-images.githubusercontent.com/80748482/184859792-76ba2a54-523c-40d2-bcbe-7315ce26e24c.png">

The letters `s`, `e`, and `a` were evidently the most frequent in the dataset. I found it slightly surprising that `s` was the most common letter in this dataset, ahead of all the vowels. Upon further examination however, the reason for this is because a lot of five letter words are simply plurals of four letter words, and therefore end with an `s`. 



### Brute Force Strategy
The brute force strategy was also attempted since the back-testing function was optimized enough to run all 12,972 words through it and return their scores in a timely manner. Although I did not expect to find a more optimal starter word in comparison to the letter frequency strategy, I still attempted it to be sure. 

<img width="1108" alt="screen1" src="https://user-images.githubusercontent.com/80748482/184859799-4bd6dd36-a366-4b49-8d68-9db70fa7824f.png">

To my surprise, neither the vowel or letter frequency strategies yeilded the best results. The "best" wordle starter according to the brute force strategy is `toeas`, which eliminates 95.72% of all word possibilities. Using this word as a starter could narrow the dataset of 12,972 words to just 555 words or lower. We can therefore conclude that the best wordle starter word is `toeas`.

### Extension
While `toeas` is certainly the best word to use in order to eliminate the maximum number of possible words, it will never be the final solution to a Wordle. This is because each Wordle's solution needs to be a word commonly used in the English language. Therefore, only 2,315 words out of the 12,900 can actually be the solution to the Wordle. For people who want to have a chance of guessing a Wordle on their first attempt, we would have to find a word that is both optimal and is present in the `answers` dataset. Seeing as brute force strategy yeilded the highest scoring words, I decided to use that again with the `answers` dataset. 

<img width="1102" alt="screen2" src="https://user-images.githubusercontent.com/80748482/184859805-e4f282aa-ee20-41a9-90ac-9621ba4e1807.png">

The best possible answers are `uraei` and `aurei`, which were both the best words in the possible words dataset when using the vowel strategy. In all honesty, I am not familiar with the majority of the best possible answers, but according to Wordle, they are commonly used in the english language and could someday, be the "mystery wordle". 

## Results
From the results of the brute force strategy, the best wordle starter word was determined to be `TOEAS`. Like you, I have never heard of this word before, but it refers to the "toea", a monetary unit of Papua New Guienea. Now while guessing `TOEAS` will eliminate the number of possible guesses by 95.72%, it will more than likely never be the actual mystery word, meaning that this strategy makes it nearly impossible to guess the worlde on your first attempt. Guessing `uraei` or `aurei` on the other hand, gives you the possibility of guessing the Wordle on your first attempt and also eliminating 95.08% of all possible words.

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
