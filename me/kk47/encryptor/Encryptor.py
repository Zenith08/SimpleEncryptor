import EncryptionEngine as encryp #@UnresolvedImport
'''
Created on May 22, 2019

@author: kaide
'''

#Executable part
print("Welcome to the encryption service.")

choice = ""

encMap = encryp.generateMapping(389598023049829045)

print(encryp.generateMapping(0))
print(encryp.decryptMapping(0))

while(choice != "Q"):
    print("What would you like to do?")
    print("(E)ncrypt text.")
    print("(D)ecrypt text.")
    print("(Q)uit")
    
    choice = input("").upper()
    
    if(choice == "Q"):
        break
    elif(choice == "E"):
        text = input("What should be encrypted?\n")
        seed = input("What key do you want to use?\n")
        print(f'Plan is to encrypt {text} with seed {seed}')
        encryp.encryptText(text, seed)
        #Now encrypt it
    elif(choice == "D"):
        text = input("What is being decrypted?\n")
        seed = input("What seed did this use?\n")
        print(f'Attempt to decrypt {text} with seed {seed}')
        encryp.decryptText(text, seed)
        #decrypt it
        
print("Thanks, goodbye.") #Maybe one day it will write to a file.