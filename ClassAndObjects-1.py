#Objects and Classes
#Lesson-1
#This is how a class is defined, in below code, Robot is a class and introduce_self
#is a function
class Robot:
    def introduce_self(self):
        print("My name is "+self.name)

#How to create objects, below r1 and r2 are objects and name, color, weight are
#attributes 
r1=Robot()
r1.name="Tom"
r1.color="Red"
r1.weight=30

r2=Robot()
r2.name="Jerry"
r2.color="Green"
r2.weight=40

r1.introduce_self()
r2.introduce_self()
