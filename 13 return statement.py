def Order(itemname):
    if(itemname=="Chicken Burger"):
        return 1
itemname=input("Enter the item name ")
result=Order(itemname)
print("Result is ",result)
if (result==1):
 print("5$,Thank you for shopping")
