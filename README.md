# Hangman Game
- Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting letters within a certain number of guesses.<br>
- This is a <q><b>Python</b></q> Language approach to the game.<br>
- Here the terminal generates the word using the nltk library and the user has to make guesses accordingly.

## Libraries Used
- [Numpy](https://numpy.org/doc/)
```python
import numpy as np
```
Installation process
```
pip install numpy
```
- [Random](https://docs.python.org/3/library/random.html)
```python
import random
```
Installation process ( should already be there in the system,if not follow the below steps )
```
pip install random
```
- [Natural Language Tool Kit / nltk](https://www.nltk.org/)
```python
import nltk
nltk.download('names')
from nltk.corpus import names
```
Installation process
```
pip install nltk
```
### Requirements
- Any IDE that can run Python 3
- Python 3.1 or above
- All Libraries installed prior to running of the code. If not done, follow the steps mentioned [here](https://github.com/Mikeyzgoat/hangman_game/new/main?readme=1#libraries-used).

### Rules
- A word is selected randomly from an array of words.
- Assume the word is `N` Letters long, then the maximum allowed number of wrong guesses will be `N-1`.
- All occurrences of a letter will be removed when right guess is made

### How multiple occurences of a letter are removed
```python
try:
  while True:
    word.remove(guess)
except ValueError:
  pass
word_length = len(word) # length of the remaining characters are updated accordingly
```
#### Created by [Mikey](https://github.com/Mikeyzgoat)
