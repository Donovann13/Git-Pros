class Code:

    year = 404

    def __init__(self,num=input("\nEnter a 3-digit num you like: \n"),month=input("Enter the num of your month of birth (like '03' for March): \n"),day=input("Enter the num of your day of birth (like '26' for 26th day of your month of birth): \n"),run1=None,run2=None,run3=None):

        if num.isalpha() or len(num) != 3:
            print("\nInvalid input for a 3-digit num!\n")
            self.run1 = False
        elif num.isdigit():
            self.num = num
            self.run1 = True
        else:
            print("\nInvalid input for a 3-digit num!\n")
            self.run1 = False
        if month.isalpha() or len(month) != 2:
            print("\nInvalid input for month of birth!\n")
            self.run2 = False
        elif month.isdigit()  and int(month) <= 12 and int(month) > 0:
            self.month = month
            self.run2 = True
        else:
            print("\nInvalid input for month of birth!\n")
            self.run2 = False
        if day.isalpha() or len(day) != 2:
            print("\nInvalid input for day of birth!\n")
            self.run3 = False
        elif day.isdigit() and int(day) <= 30 and int(day) > 0:
            self.day = day
            self.run3 = True
        else:
            print("\nInvalid input for day of birth!\n")
            self.run3 = False

    def showcode(self):
        print(f"\n---Your uni code: {Code.year}-{self.num}-{self.month}-{self.day}---\n")


mycode = Code()
if mycode.run1 == True and mycode.run2 == True and mycode.run3 == True:
    Code.showcode(mycode)