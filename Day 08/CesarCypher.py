#Cesar Cypher
from asyncio import FastChildWatcher
from sympy import true


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run_program = True

def encrypt(msg, shift):
    encrypted_msg = ""
    for i in msg:
        try:
            index = alphabet.index(i)
            new_index = index + shift
            while new_index > len(alphabet):
                new_index -= len(alphabet)   
            encrypted_msg += alphabet[new_index]
        except:
            encrypted_msg += i
    print(f"The encoded text is: {encrypted_msg}")

def decrypt(msg, shift):
    decrypted_msg = ""
    for i in msg:
        try:
            index = alphabet.index(i)
            new_index = index - shift
            while new_index < 0:
                new_index += len(alphabet)
            decrypted_msg += alphabet[new_index]
        except:
            decrypted_msg += i
    print(f"The decoded text is: {decrypted_msg}")

while(run_program):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    continue_program = input("\n Restart program? (y/n)")
    if(continue_program == "y"):
        run_program = True
    else:
        run_program = False
