"""
A string is simply a series of characters. Anything inside quotes 
is considered a string in Python, and you can use single or
 double quotes around your strings like this:
 """
print("Declaration of the String in Python")
message='This is the String'
print(message)

#Changing case of the String on Python
print(message.title())
"""
By using title Function we can start a String
with the UperCase letter
"""

#Other Method of changing A String

name='raymond'
print(name.upper())
print(name.lower())

"""
Upper Function will be used to Change String into Capital Letter
While
lower(), Function used to change a String on the lower Case

"""
"""
Concatenation of the Sting in Python
"""
first_name='Zabella'
last_name='Seif'
full_name=first_name + " "+ last_name
print(full_name)
print(full_name.upper()) #Making the Full Name as A Capital Letter


#Adding Whitespace to Strings with Tabs or Newlines
print("This is Python")
print('\tPython')
print('\t'+ full_name)

#Adding a new Line in Python
print(name)
print('\nname: \tfirst_name: \nlast_name')