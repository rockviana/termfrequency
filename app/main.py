import os
import string
from string import punctuation
from nltk import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

def readFile(path):
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

def printReport(report):
    for index,attr in enumerate(report):
        print('{}. {}: {}'.format(getAlphabetPosition(index), attr, report[attr]) )

def calcFrequencyTerms(text):
    words = word_tokenize(text)
    words = sanitizeterms(words)
    frequency = FreqDist(words)
    return dict(frequency)

if __name__ == "__main__":
    import sys

    try:
        file = ' '.join(sys.argv[sys.argv.index('-f') + 1:]) or None
    except Exception:
        print('Arquivo de texto não informado')

    article = readFile(file)
    phrases = sent_tokenize(article, language='english')

    report = {}
    for index, phrase in enumerate(phrases,1):
        terms = calcFrequencyTerms(phrase)
        for term in terms:
            report[term] = report.get(term) or {'counter':0,'occurrences':[]}
            report[term]['counter'] += terms[term]
            report[term]['occurrences'].append(index)

    for term in report:
        report[term] = {report[term]['counter']:report[term]['occurrences']}

    printReport(report)