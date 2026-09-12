# ● ┌ ─ ┐ │ └
import random

sum= 0
dices = []
Dice = {
    1:      
       ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────`")
        
    ,2:
       ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────`")

    ,3:
       ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────`")

    ,4:
       ("┌─────────┐",
        "│  ●    ● │",
        "│         │",
        "│  ●    ● │",
        "└─────────`")
        
    ,5:
       ("┌─────────┐",
        "│  ●    ● │",
        "│    ●    │",
        "│  ●    ● │",
        "└─────────`")

    ,6:
       ("┌─────────┐",
        "│  ●    ● │",
        "│  ●    ● │",
        "│  ●    ● │",
        "└─────────`")}

num = int(input("Enter the number of dices: "))

for i in range(num):
    dice = random.randint(1, 6)
    dices.append(dice)
    sum += dice

for i in range(5):
    for j in range(num):
        print(Dice[dices[j]][i], end=" ")
    print()

print(f"Sum of dices:{sum}")