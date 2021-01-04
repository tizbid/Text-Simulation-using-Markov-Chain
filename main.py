### Markov Chain for text simulation

import numpy as np
import pyttsx3 as pt

#initialize speech engine                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
engine = pt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Speech extracts
new_year_quotes = open('text.txt', encoding= 'utf8').read()
 
lines= new_year_quotes.split()

#make 2-word sequence
def make_pairs(lines):
    for i in range(len(lines)-1):
        yield(cut[i], cut[i + 1])

pairs= make_pairs(lines)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    
    else:
        
        word_dict[word_1] = [word_2]
    
first_word = np.random.choice(lines)


chain = [first_word]

n_words = 50

#Build chain
def convert_to_string():
    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))
        
    new_speech= ' '.join([str(elem) for elem in chain])
    
    return new_speech



new_speech= convert_to_string()   
print(new_speech)

engine.say(new_speech)  #Hquoteear the 
engine.save_to_file(new_speech, 'test.mp3') #Save it as an audio file.
engine.runAndWait()