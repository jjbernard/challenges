from data import DICTIONARY, LETTER_SCORES
import re

# Create a dictionary for the highest score word

highest_score_word = {'word': None, 'score': 0}

# Use a regexp to remove non letter characters (hyphens)

regex = re.compile('[^a-zA-Z]')

for line in open(DICTIONARY, "r"):
    # change word to uppercase
    word = line.upper().rstrip()
    # apply regexp
    word = regex.sub('', word)
    # initialize score
    score = 0
    # compute score for current word
    for i in range(len(word)):
        score += LETTER_SCORES[word[i]]
    # check if word is longer than highest recorded word
    if score >= highest_score_word['score']:
        highest_score_word['word'] = word
        highest_score_word['score'] = score

print('The word with the highest score is: {} with a score of {}'.format(highest_score_word['word'], str(highest_score_word['score'])))