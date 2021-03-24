# Simple python program to demonstrate Queue implementation in Python

queue = [] 
  
queue.append('a') 
queue.append('b') 
queue.append('c') 
  
print("Initial queue") 
print(queue) 

print("\nElements dequeued from queue") 
print(queue.pop(0)) 
print(queue.pop(0)) 
print(queue.pop(0)) 
  
print("\nQueue after removing elements") 
print(queue) 
  
