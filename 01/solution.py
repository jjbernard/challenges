from data import DICTIONARY, LETTER_SCORES
import re

# Create a dictionary with the highest score word

highest_score_word = {'word': None, 'score': 0}
regex = re.compile('[^a-zA-Z]')

for line in open(DICTIONARY, "r"):
    word = line.upper().rstrip()
    word = regex.sub('', word)
    score = 0
    for i in range(len(word)):
        score += LETTER_SCORES[word[i]]
    if score >= highest_score_word['score']:
        highest_score_word['word'] = word
        highest_score_word['score'] = score

print('The word with the highest score is: {} with a score of {}'.format(highest_score_word['word'], str(highest_score_word['score'])))