#squares.py
squares=[]
for value in range(1,10):
	square=value**2
	squares.append(square)
print(squares)


print('In Advanced WAy')
squares=[value**2 for value in range(1,11)]
print(squares)