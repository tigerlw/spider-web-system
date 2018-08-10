# -*- coding: utf-8 -*-

import re
import string
import collections



def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation + string.whitespace) for word in sentence]
    sentence = [word for word in sentence if len(word) > 1 or (word.lower() == 'a' or word.lower() == 'i')]
    return sentence

def cleanInput(content):
    content = content.upper()
    content = content.decode('utf-8')

    #content = re.sub('\\n|[[\\d+\\]]', ' ', content)
    #content = bytes(content, "UTF-8")
    #content = content.decode("ascii", "ignore")
    sentences = content.split(" ")
    #return [cleanSentence(sentence) for sentence in sentences]
    return sentences


def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content) - n + 1):
        tmp = content[i:i + n]
        word = ""
        for i in tmp:
            word = word + " " +i
        output.append(word)
    return output

def getNgrams(content, n):
    content = cleanInput(content),
    ngrams = []
    for sentence in content:
        ngrams.extend(getNgramsFromSentence(sentence, n)),
    return (ngrams)


#content = "wo shi liuwei 123 wo shi liuwei"

#title = getNgrams(content,2)

#print title

#print collections.Counter(title)


