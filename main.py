### Markov Chain for text simulation

import numpy as np
import pyttsx3 as pt

#initialize speech engine                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
engine = pt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#extract quotes
new_year_quotes = open('text.txt', encoding= 'utf8').read()
lines= new_year_quotes.split()
                                                                                                                                                                          

#make word pairs
def make_pairs(lines):
    for i in range(len(lines)-1):
        yield(lines[i], lines[i + 1])
    

pairs = make_pairs(lines)
 
#breakpoint()

word_dict = {}                             

# Append word pairs to dict
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]
        
       
#seed out first random word
first_word = np.random.choice(lines)


chain = [first_word]

n_words = 50

#Build chain
def construct_chain():
    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))
        
    new_quote= ' '.join([str(elem) for elem in chain])
    
    return new_quote



quote= construct_chain()   
print(quote)

engine.say(quote) #Listen to the quote
engine.save_to_file(quote, 'quote.mp3') #Save quote as an audio file.
engine.runAndWait()