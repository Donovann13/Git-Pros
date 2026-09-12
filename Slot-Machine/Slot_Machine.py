import random

emojies = ["🐊","🌟","🌈","🔥","💥"]
balance = 100
rowlst =[]
payout = 0

print("***********************")
print("   ----Welcome!----    ")
print("***********************")

print(f"--Your balance is ${balance}\n***********************")

while balance > 0:

    bet = input("Enter the amount of your bet:$")

    if not bet.isdigit():
        print("Invalid input!")

    elif int(bet) <= 0:
        print("Invalid input!")

    elif int(bet) > balance:
        print("Not enough balance!\n***********************")

    else:
        balance -= int(bet)

        print()
        for i in range(3):
            rowlst.append(random.choice(emojies))
        for m in rowlst:
            print(f"- {m} -",end="")
        print()

        if rowlst[0] == rowlst[1] == rowlst[2]:
            print("\n---You won this round!---")

            for x in range(1,len(emojies)+1):
                if rowlst[0] == emojies[x-1]:
                    payout = int(bet) * x
                    balance += payout
                    print(f"---You won ${payout}!---\n")

        print(f"***********************\n--Your balance is ${balance}\n***********************")

        if balance <= 0:
            print("   ----Game over!----   ")
            print("************************")

        rowlst.clear()