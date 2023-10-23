#python for loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#----the above is a normal for loop-----



#------this is a range() function often used in for loops
for i in range(5):
    print(i)



fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")


