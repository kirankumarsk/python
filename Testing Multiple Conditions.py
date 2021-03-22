#Testing Multiple Conditions 
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:              #Will check if the element value is in a list
	print("Adding mushrooms")
if 'mango' not in requested_toppings:              #will check if the value is not in the list
	print("Add mango")
if 'extra cheese' in requested_toppings:
	print("Add more Cheese")
print("\nFinishing Making Your Pizza")