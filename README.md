# Trumpinator
#### Trumpinating the twitter. Trumpinating the blagospore.
This project aims to build on a tri-gram tweet generator some friends built. The goal is to learn Trumpian syntax and vocabulary, and construct new plausible Trump-tweets. It is highly likely that the tweets will often be offensive. If this occurs, it shouldn't be taken as an endorsement of Trump's beliefs, but rather an indictment. (TAY DID NOTHING WRONG).

## Components
#### Grammar Parsing
The first step is to use some grammar parser to build sentence trees from Trump tweets. From a generic corpus, the complexity of this task grows pretty quickly ([Catalan numbers](https://oeis.org/A000108)), but tweets are constrainted to 140 characters, limiting the space. 
The parsed grammar will be used in two ways. The first is that a Trumpian grammar will be selected for generating sentences. The second is that the parsed grammar should be used as an input to learning vector representations of Trumpian vocabulary. In other words, instead of just looking at w-2 to w+2 for context, we will try to learn relationships between noun phrases and verb phrases. 
Currently, the idea for choosing a grammar is just to have a weighted probability derived from observed frequencies for each grammar type. (Lookup table).
#### Word vectors
The current idea is to use a PoS tagged word tokenization to learn vector representations of words. It may be necessary to move to character representation if Trump often makes up new words.

## Additional Features
It would also be nice to implement 'online' learning, i.e. the model is trained on streaming twitter data rather than batched. Also there should be a tie-in to a twitter API to let the bot post on its own. 
