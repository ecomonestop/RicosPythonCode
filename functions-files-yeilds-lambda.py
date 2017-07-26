#function examples
students = []

#functions are lower case seperated by _ and keyword def is used
#You can return a value but as you see there is no return value in the function 'header' he called it but regularly ive always used a function/method signature
def get_student_titlecase():
    students_title_case = []
    for student in students:
        students_title_case.append(student.title())
    return students_title_case

def print_student_titlecase():
    print(get_student_titlecase())

#functions can have args that have default values.  e.g. student_id.  This means a caller doesnt have to pass in a value if they dont want too
#As always, you dont specify the type of the arugements, you just give it a name
def add_student(name, student_id=332):
    students.append(name)
    print(student_id)

#function using the * notation to signify that it can take in as many aguments as you want to pass it.  Notice when using the args variable name in the function
#we dont include the * anymore, only in the function signature
def var_args(name, *args):
    print(name)
    for arg in args:
        print(arg)

#function using the ** notation to signify that we want to use the  key word arguments which means we can pass in as many args as we want and also they have a name.
# The **kwargs below becomes a dectionary, where the keys are the names given to the args, and the value is the value of the args passed in
def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["job"], kwargs["company"])

#calling a function and overriding the default parameter value
add_student("Rico", 1)
#Calling a function and using the default value of the paramater
add_student("Nico")
#Calling var_args to show we can pass in as much arguments as we want
var_args("Rico", "Shelly", None, 34, 23.0)
#Calling var_kwargs to show we can pass in as much arguments as we want and naming them
var_kwargs("Rico", file="no file", job="IT", company="GE")

