import random

hangman_art = {
            1: "            \n"
               "            \n"
               "            \n",
            2: "      O     \n"
               "            \n"
               "            \n",
            3: "      O     \n"
               "      |     \n"
               "            \n",
            4: "      O     \n"
               "      |\\   \n"
               "            \n",
            5: "      O     \n"
               "     /|\\   \n"
               "            \n",
            6: "      O     \n"
               "     /|\\   \n"
               "      |     \n"}

def main():

   for char in word:
      showed.append("_")

   wrong = 0

   print(f"\nThe word has {len(showed)} letters.")
   print(" ".join(showed))
   print()

   while True:

      if wrong == 6:
         print("---Game over!---\n")
         break

      if "_" not in showed:
         print("Well played!\n")
         break

      guess = input("Enter your guess as a char: ").lower()

      if guess.isalpha() and len(guess) == 1:

         if word.count(guess) != 0:
            for i in range(len(word)):
               if guess == word[i]:
                  showed[i] = word[i]
            if wrong != 0:
               print(f"\n{hangman_art[wrong]}")
               print(f"number of wrong guesses: {wrong}")  
            elif wrong == 0:
               print(f"\nnumber of wrong guesses: {wrong}")  

         elif word.count(guess) == 0:
            wrong = wrong + 1
            print(f"\n{hangman_art[wrong]}")
            print(f"number of wrong guesses: {wrong}")  

      else:
         print("\n---Invalid input!---")
              
      print()
      print(" ".join(showed))
      print()

words = ["apple","banana","kiwi"]
word = random.choice(words)
showed = []

if __name__ == "__main__":
    main()

            