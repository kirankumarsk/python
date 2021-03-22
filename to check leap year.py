year=int(input("Enter the year:"))
show="Leap Year" if year%400==0 else "Leap Year" if year%4==0 and year%100!=0 else "Non Leap Year"
print(show)
