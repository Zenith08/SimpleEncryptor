import EncryptionEngine as encryp #@UnresolvedImport
import sys
'''
Created on May 22, 2019

@author: kaide
'''

#Functions for execution stuff
#Encrypts a file from src and saves the new copy to dest using the provided seed
def encryptFile(src, dest, seed):
    #Open both files. If this fails then quit now.
    with open(src, 'r') as source:
        with open(dest, 'w') as destination:
            #Tell the user what's happening
            print("Beginning encode of", src, "to", dest)
            encmap = encryp.generateMapping(seed) #saving the map now saves on performance later.
            
            for line in source: #Loop through the file and encrypt the file using the provided string.
                destination.write(encryp.mapString(line, encmap))
                
            destination.close()
        source.close()
    print("Completed encoding.")

#Decrypts a file from src and saves it to dest using the provided seed.
#Basically like the encryptFile but uses the decryption map.
def decryptFile(src, dest, seed):
    with open(src, 'r') as source:
        with open(dest, 'w') as destination:
            print("Beginning decoding of", src, "to", dest)
            encmap = encryp.decryptMapping(seed)
            
            for line in source:
                destination.write(encryp.mapString(line, encmap))
                
            destination.close()
        source.close()
    print("Completed decoding.")

#Max int from python 2 9223372036854775807
#The idea is this will figure out what seed was used given a known word and encrypted text put in.
def hackText(encrypted, known):
    for i in range(1000): #Loop through each possible key. Starting at 1
        result = encryp.decryptText(encrypted, str(i))
        if known in result: #If the known word is in the decrypted string
            print("The used seed was", i) #Tell the user and end the check.
            print("The text read:", result)
            return result

    print("Finished check and found nothing.")
#Executable part -----------------------------------------------------------
print("Welcome to the encryption service.")

choice = "" #What the user wants to do.

#If the user isn't trying to quit. I think break happens first but this is still useful as a fail safe.
while(choice != "Q"):
    #Print options
    print("What would you like to do?")
    print("(E)ncrypt text.")
    print("(D)ecrypt text.")
    print("(W)rite an encrypted file.")
    print("(R)ead an encrypted file.")
    print("(H)ack an encryption.")
    print("(Q)uit")
    
    #Get input. Forcing to upper case saves worrying about what the user put in.
    choice = input("").upper()
    
    if(choice == "Q"): #If the user wants to quit then let them.
        break
    elif(choice == "E"): #Encrypting text needs just the string to encrypt and a seed to use for it.
        text = input("What should be encrypted?\n")
        seed = input("What key do you want to use?\n")
        #print(f'Plan is to encrypt {text} with seed {seed}')
        result = encryp.encryptText(text, seed)
        print("Result:")
        print(result)
    elif(choice == "D"): #Decrypting text usesthe same system as encryption but reversed.
        text = input("What is being decrypted?\n")
        seed = input("What seed did this use?\n")
        #print(f'Attempt to decrypt {text} with seed {seed}')
        result = encryp.decryptText(text, seed)
        print("Result:")
        print(result)
    elif(choice == "W"):
        #Encrypting a file needs to know the source file, and seed. We generate the output name so it isn't more inputs for the user.
        target = input("What file should be encrypted?\n")
        dest = target + "-enc.txt"
        seed = input("What key should be used?\n")
        encryptFile(target, dest, seed)
    elif(choice == "R"): #Decrypting a file we do need to know what the destination is so that it is properly named.
        target = input("Enter the encrypted file name.\n")
        dest = input("What should the decrypted file be called?\n")
        seed = input("What encryption seed was used?\n")
        decryptFile(target, dest, seed)
    elif(choice == "H"):
        text = input("Enter encrypted text.\n")
        known = input("Enter a word you know exists.\n")
        hackText(text, known)
    else:
        print("That is not an option.") #If they didn't choose an option then just let them try again.
    
print("Thanks, goodbye.") #If they are exiting the program tell them that's okay.
