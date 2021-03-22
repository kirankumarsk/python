#While Statement
'''
Syntax:
while(Condition is True):
	Statement
'''

#Finding the Sum of Numbers
num=int(input('Enter the Value of Number='))
if (num<=0):
	print("Enter the valid Value")
else:
	sum=0
	while(num>0):
		sum+=num
		num-=1
print(sum)