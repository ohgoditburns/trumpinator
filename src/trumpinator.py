

import nltk
import json
import logging
import warnings
from nltk.tokenize import word_tokenize


def ngram(tokenized_content, n):
    ngram_mod = nltk.model.NgramModel(n, tokenized_content)
    txt_format = nltk.text.Text(tokenized_content)
    return ngram_mod, txt_format


def gen_phrase(model, num_words, starter_word=None):
    warnings.simplefilter("ignore")
    if starter_word is None:
        rand_start = model.generate(100)[-2:]
        quote = ' '.join(model.generate(num_words, rand_start))
    else:
        quote = ' '.join(model.generate(num_words, starter_word))
    print(quote)


def main():
    # Load up txt files
    speech_file = open('trump-speeches/speeches.txt').read()
    tweets = json.load(open('trump_tweets.json'))
    tweet_list = []
    for tweet in tweets:
        tweet_list.append(tweet['text'])
    tweet_list = ' '.join(tweet_list)

    # Tokenize
    logging.info('Formatting training text')
    speech_token = word_tokenize(speech_file)
    tweet_token = word_tokenize(tweet_list)

    # Train trigram models
    logging.info('Setting up models')
    speech_gram, speech_format = ngram(speech_token, 3)
    tweet_gram, tweet_format = ngram(tweet_token, 3)

    # Generate responses
    cont = True
    while cont:
        response = input("Hello sir, what can I Trumpinate for you?: ")
        num_words = input("And how many words should I write?: ")

        # Print Phrases
        gen_phrase(speech_gram, int(num_words), starter_word=[response])
        print('')
        gen_phrase(tweet_gram, int(num_words), starter_word=[response])
        more = input("Would you like to generate more? (Yes, No): ")
        if more != 'Yes':
            cont = False

if __name__ == '__main__':
    main()
