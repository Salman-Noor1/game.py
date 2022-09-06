import random
count = 0

while count < 5:
    guess = input("enter the number ")
    answer = int(guess)
    if answer == 5:
        print("You are correct")
        break
    else:
        print("You are wrong")
    count +=1

print("Game finish")