import string #gets us access to letters
import random
'''
Created on May 22, 2019
@author: Kaiden Richardson
'''
#As a fun fact there are 100! possible encryption maps that can be generated. Thats
#9.3326215443944152681699238856267*10^157‬ combinations.
#this is supposed to have functions to encrypt and decrypt the text input
#Generate an encryption map of one character to another character.
#The random seed is equivilant to the key which will be used.
def generateMapping(seed):
    random.seed(seed) #Seed our random
    randMap = {} #Create our output map.
    #Generates a series of nonrepeating random numbers which are all going to be valid chars
    randoms = random.sample(range(len(string.printable)), len(string.printable))
    
    index = 0 #Index in the random value array.
    
    for let in string.printable: #This now creates the map using the original characters and then the mapped random ones.
        randMap.setdefault(let, string.printable[randoms[index]])
        index+=1
    #Return the map so it can be used.
    return randMap

#This is all the exact same code as encryption except instead of map[letter] = random we do map[random] = letter.
#This makes it the exact opposite of the encryption map.
def decryptMapping(seed):
    random.seed(seed)
    randMap = {}
    randoms = random.sample(range(len(string.printable)), len(string.printable))
    
    index = 0
    
    for let in string.printable:
        randMap.setdefault(string.printable[randoms[index]], let)
        index+=1
    
    return randMap

#Encrypt and decrypt text uses the generated maps and then applies this mapping to the string.
def encryptText(text, seed):
    encrypMap = generateMapping(seed) #Get map
    encExport = mapString(text, encrypMap) #Encode string
    
    return encExport #Return for use later.

def decryptText(text, seed):
    decrypMap = decryptMapping(seed)
    
    decrExport = mapString(text, decrypMap)
    
    return decrExport

#For a string, use the provided char map to encrypt it.
def mapString(text, mapping):
    encExport = "" #Default blank string
    
    for l in text: #For each letter
        encExport+=mapping.get(l, l) #Get its mapped property and add it to the export string.
    
    return encExport
