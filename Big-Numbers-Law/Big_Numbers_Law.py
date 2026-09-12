import random

print()

s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0

options = (1,2,3,4,5,6)
rollnum = int(input("Enter the number of rolls: "))

for i in range(rollnum):
    roll = random.choice(options)
    if roll == 1:
        s1 += 1
    elif roll == 2:
        s2 += 1
    elif roll == 3:
        s3 += 1
    elif roll == 4:
        s4 += 1
    elif roll == 5:
        s5 += 1
    elif roll == 6:
        s6 += 1
print()

print(f"1: {s1}", end=" ")
for square in range(int(s1/100)):
    print("■", end="")
print()

print(f"2: {s2}", end=" ")
for square in range(int(s2/100)):
    print("■", end="")
print()

print(f"3: {s3}", end=" ")
for square in range(int(s3/100)):
    print("■", end="")
print()

print(f"4: {s4}", end=" ")
for square in range(int(s4/100)):
    print("■", end="")
print()

print(f"5: {s5}", end=" ")
for square in range(int(s5/100)):
    print("■", end="")
print()

print(f"6: {s6}", end=" ")
for square in range(int(s6/100)):
    print("■", end="")
print()
print()

print(f"1 probability: {s1/rollnum*100:.2f}%")
print(f"2 probability: {s2/rollnum*100:.2f}%")
print(f"3 probability: {s3/rollnum*100:.2f}%")
print(f"4 probability: {s4/rollnum*100:.2f}%")
print(f"5 probability: {s5/rollnum*100:.2f}%")
print(f"6 probability: {s6/rollnum*100:.2f}%")
print()
