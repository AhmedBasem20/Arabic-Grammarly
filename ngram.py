from nltk import word_tokenize
import nltk
import pandas as pd
import re

def read_articles(path):
    """
    read the articles file and return a list of tokens
    """
    arabic_df = pd.read_csv(path)
    text = ''
    for i in range(len(arabic_df)):
        if(isinstance(arabic_df.loc[i].articles, str)):
            text += re.sub('[?.",;:]', '', arabic_df.loc[i].articles) + ' '

    tokens = word_tokenize(text)
    vocab = set(tokens)
    return tokens


def ngram_model(tokens):
    """
    generating unigram and bigram csv files from the supplied tokens
    """
    #unigram dictionary
    freq = nltk.FreqDist(tokens)
    
    #bigram dictionary
    bigrams = nltk.bigrams(tokens)
    bifreq = nltk.FreqDist(bigrams)

    df = pd.DataFrame(freq.values(), index = freq.keys(), columns =['count'],)
    df.index.name = 'ngram'
    df.to_csv('unigram2.csv')

    bidf = pd.DataFrame(bifreq.values(), index = bifreq.keys(), columns =['count'],)
    bidf.index.names = ['gram1','gram2']
    bidf.to_csv('bigram2.csv')


tokens = read_articles('F:/Graduation Project/Echorouk_articles.csv')
ngram_model(tokens)
print(str(len(tokens)) +" "+ str(len(set(tokens))))