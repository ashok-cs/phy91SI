import re
import numpy as np

def parse_sample(text,words_only=False,sort_list=False):
    text=re.sub('-',' ',text)
    words=text.split()     
    if words_only:
        words=[re.sub('[,’`.!"“\':;?()\[\]@+*^#$~{}_><]','',word.lower()) for word in words]
    if sort_list:
        words=sorted(words)

    return words


def count_freq(words):
    c=[]
    w=[]
    for word in words:
        if word not in w:
            w.append(word)
            c.append(words.count(word))    
    return w,c


#Test
f=open("sample","r")
text=f.read()
f.close()

    
words=parse_sample(text,words_only=True,sort_list=True)
print(words)    
w,c=count_freq(words)
print(dict(zip(w,c)))
print(np.mean(c))
print(np.std(c))
print(np.median(c))