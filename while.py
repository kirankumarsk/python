# While Statement

num = int(input("Enter The Value: "))
if (num<=0):
    print("Enter The Valid Value")
else:
    total=0
    while(num>=0):
        total+=num
        num-=1
print("The Sum of All numbers are: ", total)

