def show(balance):
    print(f"\n---Your balance is ${balance}---\n")

def deposit():
    amount = input("\n---Enter the amount: ")
    if amount.isdigit():
        if int(amount) > 0:
            return int(amount)
        else:
            print("\n---The amount must be greater than zero!---\n")
            return 0
    else:
        print("\n---Invalid input!---\n")
        return 0

def withdraw():
    amount = input("\n---Enter the amount: ")
    if amount.isdigit():
        if int(amount) > balance:
            print("\n---You can't withdraw the amount of money that is greater than your balance!---\n")
            return 0
        if int(amount) > 0:
            return int(amount)
        else:
            print("\n---The amount must be greater than zero!---\n")
            return 0
    else:
        print("\n---Invalid input!---\n")
        return 0


if __name__ == "__main__":

    balance = 0

    while True:

        print("********************")
        print("    Banking Menu    ")
        print("********************")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("********************")

        option = input("Enter an option: ")

        match option:
            case "1":
                show(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw()
            case "4":
                print("\n---Thank you for your time!---\n")
                break
            case _:
                print("\n---Invalid input!---\n")