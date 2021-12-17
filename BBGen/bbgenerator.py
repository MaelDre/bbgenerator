from __future__ import print_function
import random

buzz = ('les NFT', 'le web3',
    'la crypto-monnaie', 'la greentech', 'le deep learning', 'le iot')
adjectives = ('nouvelle génération', '5.0', 'self-service', 'intégré', 'end-to-end')
adverbs = ('fondamentalement', 'grandement', 'sérieusement', 'rapidement',
    'seriously')
verbs = ('accélère', 'améliore', 'disrupte', 'digitalise', 'booste', 'révolutionne')

def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([buzz_terms[0], sample(adjectives), sample(verbs), sample(adverbs),
         buzz_terms[1]])
    return phrase.title()

if __name__ == "__main__":
    print(generate_buzz())