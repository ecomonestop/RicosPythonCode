studentsWithAddMethod = []

#Simplest class.  Classes are defined by using keyword class and a name.  Convention is name begins with a uppercase letter. finally, a : and its body indented on the next line
#pass is a keyword that says to do nothing.  Good for placeholder in classes or functions
class SimpleStudent:
    pass

#self is like this in other languages.  its explicitly declared in the method signature, but implicitly passed in when calling the method with an instance of the class.
#I'm not sure yet if self is required in all methods signatures or not.
class StudentWithAddMethod:
    def add_student(self, name, id=1):
        student = {"fName": name, "id": id}
        studentsWithAddMethod.append(student)
#creating an instance
myStu = StudentWithAddMethod()
#note you dont have to pass in the arg self as its implicitly implied.
myStu.add_student("Rico")
print(studentsWithAddMethod)

# a more complete Student class.  example shows how to use the __init__ special method to override the default constructor.
# also, it shows __str__ as a way to override the "toString" method.  toString from Java seems to be equivlent to __str__ in python
students = []
class Student:
    #Example of a class Attribute.  This is the same accross all instances
    school_name = "Bates Elementary"

    def __init__(self, name, id=1):
        #name and student_id are instance attributes.  They change with each instance.  init them here in __init__ makes the available to other methods of the class for the duration of the instnace life
        self.name = name
        self.student_id = id
        students.append(self)
    
    def __str__(self):
        return "Student " + self.name

    def get_name_capitalized(self):
        return self.name.capitalize()

    def get_school_name(self):
        #note you still have to use self in order to access class attributes within the class as shown below
        return self.school_name

myBetterStudent = Student("Rico")
print(myBetterStudent)
#notice you can access class attributes without a particular instance i.e. same as Java's classes static variables
print(Student.school_name)







