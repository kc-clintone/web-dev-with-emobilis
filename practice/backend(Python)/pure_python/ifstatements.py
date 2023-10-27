#if statements

#basic
x = 10
if x > 5:
    print("x is greater than 5")

#if with else
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

#if, elif, else
x = 3
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

#nested if statements
x = 10
if x > 5:
    print("x is greater than 5")
    if x == 10:
        print("x is equal to 10")

