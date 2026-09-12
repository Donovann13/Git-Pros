import random 
import time

options = ("rock","paper","scissors")

D = 0 
CW = 0 
HW = 0

human_option = input("Enter your option (rock/paper/scissors): ")

while True:

    if not human_option in options:

        print("Your option is not considered.")
        human_option = input("Enter your option (rock/paper/scissors/q to quit): ")
        if human_option.lower() == "q":
            break
        
    else:
        computer_option = random.choice(options)

        if human_option == "rock":
            if computer_option == "paper":
                CW += 1
                print(f"Yours was {human_option} and computer's was {computer_option}.\nComputer won!")
                time.sleep(1.5)
                print(f"Draws:{D}-CW:{CW}-HW:{HW}")
            elif computer_option == "scissors":
                HW += 1
                print(f"Yours was {human_option} and computer's was {computer_option}.\nYou won!")
                time.sleep(1.5)
                print(f"Draws:{D}-CW:{CW}-HW:{HW}")
            elif computer_option == "rock":
                D += 1
                print(f"You both chose {computer_option}.\nDraw!")
                time.sleep(1.5)
                print(f"Draws:{D}-CW:{CW}-HW:{HW}")

            human_option = input("Enter your option (rock/paper/scissors/q to quit)...")
            if human_option.lower() == "q":
                break

        elif human_option == "paper":
            if computer_option == "scissors":
                CW += 1
                print(f"Yours was {human_option} and computer's was {computer_option}.\nComputer won!")
                time.sleep(1.5)
                print(f"Draws:{D}-CW:{CW}-HW:{HW}")
            elif computer_option == "rock":
                HW += 1
                print(f"Yours was {human_option} and computer's was {computer_option}.\nYou won!")
                time.sleep(1.5)
                print(f"Draws:{D}-CW:{CW}-HW:{HW}")
            elif computer_option == "paper":
                D += 1
                print(f"You both chose {computer_option}.\nDraw!")
                time.sleep(1.5)
                print(f"Draws:{D}-CW:{CW}-HW:{HW}")

            human_option = input("Enter your option (rock/paper/scissors/q to quit)...")
            if human_option.lower() == "q":
                break

        elif human_option == "scissors":
            if computer_option == "rock":
                CW += 1
                print(f"Yours was {human_option} and computer's was {computer_option}.\nComputer won!")
                time.sleep(1.5)
                print(f"Draws:{D}-CW:{CW}-HW:{HW}")
            elif computer_option == "paper":
                HW += 1
                print(f"Yours was {human_option} and computer's was {computer_option}.\nYou won!")
                time.sleep(1.5)
                print(f"Draws:{D}-CW:{CW}-HW:{HW}")
            elif computer_option == "scissors":
                D += 1
                print(f"You both chose {computer_option}.\nDraw!")
                time.sleep(1.5)
                print(f"Draws:{D}-CW:{CW}-HW:{HW}")
            
            human_option = input("Enter your option (rock/paper/scissors/q to quit)...")
            if human_option.lower() == "q":
                break