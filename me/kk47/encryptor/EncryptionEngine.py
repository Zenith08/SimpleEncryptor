import string #gets us access to letters
import random
'''
Created on May 22, 2019

@author: kaide
'''
#this is supposed to have functions to encrypt and decrypt the text input
def generateMapping(seed):
    random.seed(seed)
    randMap = {"": ""}
    randoms = random.sample(range(len(string.ascii_letters)), len(string.ascii_letters))
    
    index = 0
    
    for let in string.ascii_letters:
        randMap.setdefault(let, string.ascii_letters[randoms[index]])
        index+=1
    
    return randMap

def decryptMapping(seed):
    random.seed(seed)
    randMap = {"": ""}
    randoms = random.sample(range(len(string.ascii_letters)), len(string.ascii_letters))
    
    index = 0
    
    for let in string.ascii_letters:
        randMap.setdefault(string.ascii_letters[randoms[index]], let)
        index+=1
    
    return randMap

def encryptText(text, seed):
    encrypMap = generateMapping(seed)
    encExport = ""
    
    for l in text:
        encExport+=encrypMap.get(l, l)
    
    print(encExport)
    return encExport

def decryptText(text, seed):
    decrypMap = decryptMapping(seed)
    
    decrExport = ""
    
    print(decrypMap)
    
    for l in text:
        decrExport+=decrypMap.get(l, l)
    
    print(decrExport)
    
    return decrExport
