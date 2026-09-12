import random

fruits = ("apple","banana")
word = random.choice(fruits)
wordshow = []

for char in word:
    wordshow.append("-")
for char in wordshow:
    print(char,end=" ")

guess = input(f" The word has {len(word)} characters.\nEnter ur guess: ")

while True:

    if len(guess) == len(word): 
    
        for i in range(len(word)):
            if guess[i] == word[i]:
                print(f"Character {word[i]} in place {i+1} is correct.")
                wordshow[i] = word[i]

        if wordshow.count("-") == 0:
            for char in wordshow:
                print(char,end=" ")
            print("\nYou found the word!")
            while True:
                answer = input("Enter the word for the last time correctly to end the game: ")
                if answer == word:
                    print("Nice job!\n")
                    break
            break

        for char in wordshow:
            print(char,end=" ")

        guess = input("\nEnter ur guess: ")

    else:
        print("At least,Enter characters with amount of word's length.")
        guess = input("Enter ur guess: ")
        