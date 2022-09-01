boys = 300
girls = 500
maths = 100

name = input("what is your name? ")
print("Hello, " + name )
gender = input("what is your gender male , female or no one? ")


if gender == "male":
    answer = input("write your marks")
    if answer > 300:
        print("{name}, you can join the school")
        answer = input("what is your grade in maths? ")
        if answer >= 80:
            print("you pass")
            print("you can join the school.")
        elif answer >= 60:
           print("you will sit for a test")
           print("Then you can join the school.")
        elif answer >= 40:
           print(" you can join the school")
           print("But you will repeat the class.")
        else:
            print("you failed")
            print("Go to another school")
    else:
        print("you lose")
elif gender == "male":
    answer = input("write your marks")
    if answer > 300:
        print("{name}, you can join the school")
        answer = input("what is your grade in maths? ")
        if answer >= 80:
            print("you pass")
            print("you can join the school.")
        elif answer >= 60:
           print("you will sit for a test")
           print("Then you can join the school.")
        elif answer >= 40:
           print(" you can join the school")
           print("But you will repeat the class.")
        else:
            print("you failed")
            print("Go to another school")
    else:
        print("you lose")
else:
    print("quit")