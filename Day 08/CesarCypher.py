#Cesar Cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(msg, shift):
    encrypted_msg = ""
    for i in msg:
        index = alphabet.index(i)
        new_index = index + shift
        while new_index > len(alphabet):
            new_index -= len(alphabet)

        encrypted_msg += alphabet[new_index]
    print(f"The encoded text is: {encrypted_msg}")
def decrypt(msg, shift):
    decrypted_msg = ""
    for i in msg:
        index = alphabet.index(i)
        new_index = index - shift
        while new_index < 0:
            new_index += len(alphabet)

        decrypted_msg += alphabet[new_index]
    print(f"The decoded text is: {decrypted_msg}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
