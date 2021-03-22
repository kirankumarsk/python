names=[]       #creating an empty list for the names
n=int(input("How many names to be entered?"))   #number of names 
for i in range(n):         #using for loop 
  print(i+1,"Name")
  names.append(input())     #to add names in the list by using append command
s=set(names)    #set function is used to remove duplicate elememts in the list

print(s)      
