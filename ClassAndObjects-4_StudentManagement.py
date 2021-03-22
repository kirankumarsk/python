#Object oriented programming
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def getGrade(self):
        return self.grade

class Course:
    def __init__(self,name,maxStudent):
        self.name=name
        self.maxStudent=maxStudent
        self.students=[]

    def addStudent(self,student):
        if(len(self.students)<self.maxStudent):
            self.students.append(student)
            return True
        return False

    def classSize(self):
        return len(self.students)

    def averageGrades(self):
        value=0
        for student in self.students:
            value+=student.getGrade()
        return value/len(self.students)
size=int(input("Please Etner the size for class..."))

course=Course("Science",size)
while True:
    choice=input("Add Students..Enter Done to quit")
    if choice=='Done':
        break
    a=input("Enter the name of the Student..")
    b=int(input("Enter the age of the Student.."))
    c=int(input("Enter the grade of the Student.."))
    Student(a,b,c)
    course.addStudent(Student(a,b,c))

size=course.classSize()
print("List of Enrolled Students...\n")
print("Name Age Grade\n")
for i in range(0,size):
    print(course.students[i].name,course.students[i].age,course.students[i].grade)

print("====Average Grades====")
print(course.averageGrades())
