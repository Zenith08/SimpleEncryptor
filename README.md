# Basic Python Encryptor

In my programming class in grade 12, we were asked to learn a new programming language, and make a program in it. At the time, I had never used Python. I had seen it around but I had never done a project with it or properly learned it. Knowing how valuable it is, I decided to learn it and used it to make a basic, not secure, encrypting system.

## How it Works
The program takes a seed, which is then passed as a seed into a Python random number generator. The generator is then used to create a map for each printable character (ascii + a few more). Then, that is applied to the text which is to be encrypted.
For example `Hello World` encrypted with code `0` would get `.IddGplG}dT` as the output. To decrypt the text, the process is simply reversed. Assuming the seed is correct, the output will correctly return the original value.

The program also has the ability to work on text files and encrypt them. All of this is handled through the built in UI shown below.
```
What would you like to do?
(E)ncrypt text.
(D)ecrypt text.
(W)rite an encrypted file.
(R)ead an encrypted file.
(H)ack an encryption.
(Q)uit
```

###### Disclaimer: This is not secure and should only be used to have fun with your friends. It even has a built in hacking option.
