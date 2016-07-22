from __future__ import unicode_literals
import spacy
import codecs
import json

nlp = spacy.load('en')

def main():
    # Load up txt files
    #speech_file = codecs.open("../trump-speeches/speeches.txt", "r", "utf-8").read()
    tweets = json.load(open('../trump_tweets.json'))
    tweet_list = []
    for tweet in tweets:
        tweet_list.append(tweet['text'])
    tweet_list = ' '.join(tweet_list)
    doc = nlp(tweet_list)


    for i, token in enumerate(doc):
        print(
        token.orth_, token.dep_, token.head.orth_, [t.orth_ for t in token.lefts], [t.orth_ for t in token.rights])
        print("")
        if i > 20:
            break





if __name__ == '__main__':
    main()