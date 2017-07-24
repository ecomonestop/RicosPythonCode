
#Python is dynamically typed, meaning you dont have to specify the type of the variable its inferred.
f_name = "Rico"
l_name = "Romero"

#falsey and truey values
ssNum = None
#notice you dont have to check if a value = or != a None value.  None value is implied as false.  Also, empty strings, 0, and non declared variables are considered False
if ssNum:
    print("This will not run as ssNum is set to None and is a falsey value")
else:
    print("falsey value None")

#A list in Python acts a lot like resizable arrays in other langagues, but with a few more features and subtutilties
#E.g. You can mix the different types in your list, it doesnt care.  You can do slicing and other operations on lists as well.

#similar to a for each
names = ["Rico", "Nico", "Dom", "Celine"]
for name in names:
    print(name)
#The 10 says it will itterate 10 times
for x in range(10):
    print(x)
#Prints odd numbers as 1 declares the start, 10 is exclusive end, and 2 is number of steps to take during each itteration
for x in range(1, 10, 2):
    print(x)

