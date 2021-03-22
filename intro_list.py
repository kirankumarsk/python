"""
what Is a list? A list is a collection of items in a particular order. 
You can make a list that includes the letters of the alphabet,
 the digits from 0–9, or the names of all the people in your family.
 """

list=[1,45,3,34]
print(list)
#To access the value of the list element you need to specifie its index number
print(list[2])
print(list[-3])

#Using Individual Values from a List
cars=['Benz', 'Toyota','Vits','BMW']

#Manipulate list element
message='My First Car is '
print(message + " " +cars[0])

#Modifying Elements in a List
print(cars)
#By indexing list element by 0 means you will replace the first element with a new element
cars[0]='Scania'
print(cars)

#appending Elements to the End of a List(adding element in a list)
cars.append('Abood')
print(cars)


#To delete the element on the list we use del

del cars[0]
print(cars)

#removing an Item Using the pop() Method
#pop() function will allow you to remove element and use the removed element
#while del wont allow the use of the element del 
print('\n')
print('The element before removed')
print(cars)

print('\n')
print('Elements after Removed')
cars_popped=cars.pop()
print(cars_popped)


#organizing a list | Sorting a List Permanently with the sort() Method 
cars.sort()
print(cars)
numbers=[23,5,365,89,24,2,]
print(numbers)

#Sorted numbers
numbers.sort()
print(numbers)


#Printing a List in Reverse Orde
print(numbers)
numbers.reverse()
print(numbers)


#Finding the Length of a List
print('\n')
len(cars)
print(cars)