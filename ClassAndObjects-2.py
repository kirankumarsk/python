#Objects and Classes
#Lesson-1
#This is how a class is defined, in below code, Robot is a class and introduce_self
#is a function
class Robot:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight

    #This is an Example of method
    def introduce_self(self):
        print("My name is "+self.name)

#How to create objects, below r1 and r2 are objects and name, color, weight are
#attributes
r1=Robot("Tom","Green",30)
r2=Robot("Jerry","Red",40)

r1.introduce_self()
r2.introduce_self()
