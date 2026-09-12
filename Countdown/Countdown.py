import time

num = int(input("Enter a num in seconds: "))

for i in range(num,0,-1):

    sec = num % 60
    min = int((num / 60) % 60)
    hour = int(num / 3600)
    print(f"{hour:02}:{min:02}':{sec:02}\"")
    time.sleep(1)
    num -= 1
