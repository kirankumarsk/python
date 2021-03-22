#Multiple class interections
class Robot:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce_self(self):
        print("My name is "+self.name)

r1=Robot("Tom","Green",30)
r2=Robot("Jerry","Red",40)

class Person:
    def __init__(self,name,mood):
        self.name=name
        self.mood=mood
    def sit_down(self):
        self.is_sitting=True
    def stand_up(self):
        self.is_sitting=False

p1=Person("Radha","Happy")
p2=Person("Mohan","Excited")
#lets p1 has R2 Robot, The below code will add one more attribute to the
#Robot class as robot_owned
p1.robot_owned=r2
p2.robot_owned=r1
p1.robot_owned.introduce_self()
