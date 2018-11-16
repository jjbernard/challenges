from data import DICTIONARY, LETTER_SCORES
import re

def load_words():
    """Load dictionary into a list and return list"""
    list_of_words = []
    for line in open(DICTIONARY, "r"):
        list_of_words.append(line.rstrip())
    
    return list_of_words
        

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    word = word.upper()
    regexp = re.compile('[^a-zA-Z]')
    word = regexp.sub('', word)
    for i in range(len(word)):
        score += LETTER_SCORES[word[i]]
    
    return score
    

def max_word_value(list_of_words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word_value = {'word': None, 'value': 0}
    if list_of_words:
        for word in list_of_words:
            score = calc_word_value(word)
            if score >= max_word_value['value']:
                max_word_value['word'] = word
                max_word_value['value'] = score
    else:
        list_of_words = load_words()
        for word in list_of_words:
            score = calc_word_value(word)
            if score >= max_word_value['value']:
                max_word_value['word'] = word
                max_word_value['value'] = score

    return max_word_value['word'], max_word_value['value']

if __name__ == "__main__":
    maxword, maxvalue = max_word_value() 
    print('This is the word with the highest Scrabble score from the dictionary: {}'.format(maxword))
    print('The value of its Scrabble score is: {}'.format(maxvalue))
    # run unittests to validate
