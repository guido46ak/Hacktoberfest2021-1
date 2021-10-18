import random, time
print("Welcome to number guessing game !!!")
time.sleep(1)
x = random.randint(1, 101)
print("The number is generated!!!")
time.sleep(1)
print("You have 10 chances to guess")
count = 10
while count != 0:
    a = int(input("Guess the number : "))
    if a == x:
        print("You are right, correct number is ", x)
        print("Congratulations! You won")
        break
    elif a > x:
        print("The number is less than ", a)
    else:
        print("The number is greater than ", a)
    count -= 1
