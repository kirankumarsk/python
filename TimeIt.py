#In here we will explore how to measure the time to run a particualr piece
# of code for a particular nubmer of times...This is pretty useful to select
# the fastest avaialbe code to perform the same task
import timeit
num=range(1,100)
def divbyfive(num):
    if num%5==0:
        return True
    else:
        return False
xyz=(i for i in num if divbyfive(i))
print(timeit.timeit('''num=range(1,100)
def divbyfive(num):
    if num%5==0:
        return True
    else:
        return False
xyz=(i for i in num if divbyfive(i))
for i in xyz:
    x=i''',number=100000))
input("Hit Enter to find time taken in case of list comprehension:...")
print(timeit.timeit('''num=range(1,100)
def divbyfive(num):
    if num%5==0:
        return True
    else:
        return False
xyz=[i for i in num if divbyfive(i)]
for i in xyz:
    x=i''', number=100000))
