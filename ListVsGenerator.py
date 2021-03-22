#list comprehension vs generator
#In this we will learn about the differences between lists and generators
#and methods to make them in Python
import os
def clearScr():
    os.system('cls')

def divbyfive(num):
    if num%5==0:
        return True
    else:
        return False

#Part-1 generating an array to work on
num=range(1,30)
print("Hit Enter to see the values of num...")
input()
for i in num:
    print(i)

#part-2 making a list-comprehension of numbers which are divisible by 5
lc=[i for i in num]
print("Hit enter to print list-comprehension")
input()
clearScr()
print(lc)

#part-3: making list-comprehension using function in one lines
lc=[i for i in num if divbyfive(i)]
input("Hit Enter to print the list-comprehension divisible by 5")
print(lc)

#part-4 making generator using for loop in a lines
generator=(i for i in num if divbyfive(i))
input("Hit Enter to print generator...  ")
print(generator)
input("Hit Enter to see the values of generator...")
for i in generator:
    print(i)

#part-5: Creating list with double for loop in a lines
lc=[[[i,ii] for ii in lc] for i in lc]
input("Hit Enter to see the list made using double for loop...")
print(lc)

#Part-6: making tuples
lc=[i for i in num if divbyfive(i)]
lc=[[(i,ii) for ii in lc] for i in lc]
input("Hit Enter to see the tuples using list-comprehension")
print(lc)

#part-7:Making generator
generator=(((i,ii) for ii in range(5)) for i in range(5))
input("Hit Enter to print generator...")
print(generator)
input("Hit Enter to see the values...")
for i in generator:
    for ii in i:
        print(ii)
