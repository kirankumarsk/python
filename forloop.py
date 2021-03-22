# For Loop Statement
for soda in range(99,0,-1):
    if soda>1:
        print(soda,"The Bottle of Soda in the Wall ", soda,"Chupa za Soda")
        if soda>2:
            suffix=str(soda)+ " Bottle of the Soda in the wall"
        else:
            suffix="1 Bottle of the soda in the Wall"
    elif soda==1:
        print("1 Bottle of the Soda in the Wall, 1 Bottle of the Soda")
        suffix="No more Soda in the wall"
    print("Take one Down and Pass it Around",suffix)
    print("****")
