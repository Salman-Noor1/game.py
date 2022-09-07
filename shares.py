print("enter the shares")
shares = int(input())
print("enter the deposit")
deposit = int(input())

if shares > 10000:
    interest = 0.05 * shares
else:
    interest = 0.03 * shares

totalshares = interest + shares
saving = totalshares + deposit

print(totalshares)
print(saving)    

