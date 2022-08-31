# Which number is greatest in three numbers

# start

print("Enter Three Numbers")

x = input(int())
y = input(int())
z = input(int())

if x>y:
    if x>z:
        print("X is greatest")
    else:
        print("z is greatest")
elif y>z:
    print("Y is greatest")
else:
    print("Z is greatest") 