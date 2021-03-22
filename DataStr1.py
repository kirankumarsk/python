#list ORDER building
#1 Sorting
friends=["Satya","Radha","Mohan"]
friends.sort()
print(friends)

#max,min,sum
num=range(1,10)
print(max(num))
print(min(num))
print(sum(num))

#Average Finder
numlist=list()
while True:
    imp=input("Enter a number")
    if imp=='Done': break
    value=float(imp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print("Average", average)
