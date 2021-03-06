students = []

#functions are lower case seperated by _ and keyword def is used
#You can return a value but as you see there is no return value in the function 'header' he called it but regularly ive always used a function/method signature
def get_studentname_titlecase():
    students_title_case = []
    for student in students:
        students_title_case.append(student["name"])
    return students_title_case

def print_student_titlecase():
    print(get_studentname_titlecase())

#functions can have args that have default values.  e.g. student_id.  This means a caller doesnt have to pass in a value if they dont want too
#As always, you dont specify the type of the arugements, you just give it a name
def add_student(name, student_id=332):
    student = { "name" : name, "student_id": student_id }
    students.append(student)
    

#use input for console apps input

def promt_user_to_add_student():
    student_name = input("What is the students first name: ")
    student_id = input("What is the student id: ")
    add_student(student_name, student_id)

def continue_to_add_students_promt():
    continue_to_add_students = input("Would you like to add another student y/n: ")
    return continue_to_add_students

def save_file(student_name):
    try:
        f = open("student-names.txt", 'a')
        f.write(student_name + "\n")
        f.close()
    except Exception as e:
       print("Cannot save files")

def read_file():
    try:
        f = open("student-names.txt", 'r')
        for student_name in f.readlines():
            add_student(student_name)
        f.close()
    except Exception as e:
        print("could not read file")
    
# A bug is present, after 3 times of entering names you get duplicate names printed out from students list when running print_student_titlecase first time
read_file()
print_student_titlecase()
promt_user_to_add_student()
continue_to_add_students = continue_to_add_students_promt()
while True:
    if continue_to_add_students == "y":
        promt_user_to_add_student()
        continue_to_add_students = continue_to_add_students_promt()
    else:
        mySet = set()
        for student in students:
            mySet.add(student['name'])
        for student_name in mySet:
            save_file(student_name)
        break
