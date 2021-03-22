#In this example we are going to see the techniques
#to define a upper class to control Multiple Lower calsses
class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")
p=Pet("Tim",20)
p.show()
c=Cat("Jill",32)
c.show()
d=Dog("Jerry",22)
d.show()
d.speak()
