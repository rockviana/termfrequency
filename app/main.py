import os
import string
from string import punctuation
from nltk import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

def openfile(path):
    path_script = os.path.dirname(__file__)
    file_path = os.path.join(path_script, path)
    with open(file_path, 'r') as f:
        return f.read()

def sanitizeterms(terms):
    return [term for term in terms if term not in punctuation]

def getAlphabetPosition(index, alphabet=string.ascii_lowercase, batch=None):
    batch = batch or len(alphabet)
    div, mod = divmod(index, batch)
    letter = alphabet[mod]
    if div > 0:
        return getAlphabetPosition(div - 1, alphabet, batch) + letter
    return letter

def report(title,itens):
    print(title)
    for index,attr in enumerate(itens):
        print('{}. {}: {}'.format(getAlphabetPosition(index), attr, itens[attr]) )

def calcFrequencyTerms(text):
    words = word_tokenize(text)
    words = sanitizeterms(words)
    frequency = FreqDist(words)
    return dict(frequency)

if __name__ == "__main__":
    file = 'files/small.txt'
    article = openfile(file)
    articleFrequency = calcFrequencyTerms(article)
    report("Frequency by article", articleFrequency)

    phrases = sent_tokenize(article)

    for attr in articleFrequency:
        articleFrequency[attr] = {'counter':articleFrequency[attr],
                                  'counterPhrase':[0] * len(phrases)}

    for index, phrase in enumerate(phrases):
        phraseFrequency = calcFrequencyTerms(phrase)
        for attr in phraseFrequency:
            articleFrequency[attr]['counterPhrase'][index] = phraseFrequency[attr]

    for attr in articleFrequency:
        articleFrequency[attr] = {articleFrequency[attr]['counter']:articleFrequency[attr]['counterPhrase']}

    report("Frequency by article + by phrase", articleFrequency)