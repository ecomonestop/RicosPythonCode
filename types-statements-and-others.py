
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

#accessing list elements
print(names[0])

#appending new values
names.append("Shelly")

#Finding a length is in a function called len
print(len(names))

#See if a element is in a list

if "Rico" in names:
    print("Rico is in names")

# delete a value from a list - i.e. Celine value in this case
del names[3] 
print(names, " has no Celine after delete")

#bools, while loops, and break
whileCon = True
whileCounter = 0
while whileCon:
    print("hello " + str(whileCounter))
    whileCounter += 1
    if whileCounter >= 10:
        break

# dictionary examples.  dictionary is key/value pair.  Again, type doesnt matter you can mix type.  Also, you access, delete, update, and add very similar to lists
myDict = {
    "name": "Rico",
    "age": 27,
    "occupation": "Software Engineer",
    "kids": None
}
#add or update can be done this way
myDict["years on job"] = 5
#delete
del myDict["kids"]

#try and except blocks
try:
    #kids key/value deleted above will result in KeyError
    #kids = myDict["kids"]
    print("will throw an Exception bc you cant do " + 5  + "this")
except KeyError as error:
    print("A key error occurred")
    print(error)
except Exception:
    print("Exception catches everything")

#We missed tuples and sets in this example module.
#tuple is an immutable list
#a set is the same as a Set in another language






