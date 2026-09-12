import random
import string

def encrypt(sen):
    answer = ""
    for letter in sen:
        index = alphabet.index(letter)
        answer += keys[index]
    print(f"Encrypted massage: {answer}")

def decrypt(sen):
    answer = ""
    for letter in sen:
        index = keys.index(letter)
        answer += alphabet[index]
    print(f"Decrypted massage: {answer}")


alphabet = []
for i in string.digits:
    alphabet.append(i)
for i in string.ascii_lowercase:
    alphabet.append(i)
for i in string.ascii_uppercase:
    alphabet.append(i)
for i in string.punctuation:
    alphabet.append(i)
alphabet.append(" ")

keys = alphabet.copy()
random.shuffle(keys)

while True:
    option = input("\nEnter your option.\nEncrypt(1)/Decrypt(2)/Quit(q): ")

    if option == "1":
        print()
        sentance = input("Enter your sentance to encrypt: ")
        encrypt(sentance)

    elif option == "2":
        print()
        sentance = input("Enter your sentance to decrypt: ")
        decrypt(sentance)

    elif option.lower() == "q":
        print()
        break
         
    else:
        print("---Invalid input!---\n")