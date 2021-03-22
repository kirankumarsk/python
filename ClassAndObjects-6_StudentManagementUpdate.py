class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def getGrage(self):
        return self.grade

class Course:
    def __init__(self,name,maxStudent):
        self.name=name
        self.maxStudent=maxStudent
        self.students=[]

    def addStudent(self,student):
        if len(self.students)<self.maxStudent:
            self.students.append(student)
            return True
        return False

    def averageGrades(self):
        value=0
        for student in self.students:
            value+=student.getGrage()
        return value/len(self.students)

    def averageAge(self):
        value=0
        for student in self.students:
            value+=student.age
        return value/len(self.students)

while True:
    #Student addition program
    choice=input("Enter 0 to Load existing Students\nEnter 1 to Add more Students\nEnter Done to EXIT ")
    if choice=="Done": break
    choice=int(choice)
    if(choice==0):
        s1=Student("Tim",21,98)
        s2=Student("Jill",22,96)
        s3=Student("Johny",21,86)
        course=Course("Science",3)
        course.addStudent(s1)
        course.addStudent(s2)
        course.addStudent(s3)
        print("==========================================")
        print("Name   Age  Grades")
        for i in range(0,2):
            print(course.students[i].name,course.students[i].age,course.students[i].grade)
        print("Average Grades= ",course.averageGrades())
        print("Average Age of Students = ",course.averageAge())
        input()
    if(choice==1):
        courseName=input("Please ENTER the NAME of Course...")
        maxEntry=int(input("ENTER the max no of Students..."))
        course=Course(courseName,maxEntry)
        for i in range(0,maxEntry):
            a=input("Enter the Name of Student...")
            b=int(input("Enter the age..."))
            c=int(input("Enter the Grades..."))
            course.addStudent(Student(a,b,c))
            print("Plese press ENTER to continue add more student")
            print("Plese enter 'Done' to finish the Entery ")
        #Results printing
        print("Name   Age  Grade")
        print("-----------------")
        for i in range(0,maxEntry):
            print(course.students[i].name,course.students[i].age,course.students[i].grade)
        print("Average Grades= ",course.averageGrades())
        print("Average Age of Students = ",course.averageAge())
