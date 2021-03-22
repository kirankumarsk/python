fhand=open("Password.txt","a+")
fhand.truncate()
import os
os.system('cls')
choice=int(input("""
*******************************************
*************** Welcome *******************
Enter 1 to Add new username and password
Enter 2 to Sign-in
Enter 0 to clear database
Enter 99 to Quit..."""))
def userExists(username):
    fhand=open("Password.txt","r")
    for line in fhand:
        flag=0
        line=line.rstrip()
        words=line.split()
        if username in words:
            flag=1
            print("User exists")
            break
    return flag
def passwordValidation(password):
    special=['!','@','#','$','%','&']
    val=True
    if len(password)<6:
        print("Atleast 6 letters are needed...")
        val=False
    if len(password)>20:
        print("Maximum 20 letters are allowed...")
        val=False
    if not any(char.isdigit() for char in password):
        print("Atleast 1 numeral needed...")
        val=False
    if not any(char in special for char in password):
        print("Atlease 1 special sysmbol is needed...")
        val=False
    if val:
        return val
#Main program
while True:
    if choice==99:
        os.system('cls')
        print("******************* Thank You *******************")
        quit()
    if choice==0:
        protection=input("Enter the MASTER PASSWORD to clear database..")
        if protection=="ellipses@007A":
            fhand=open("Password.txt","w+")
            fhand.truncate()
            print("Database Cleared")
        else:
            print("You are not authorised to clear database")
    if choice==1:
        fhand=open("Password.txt","a+")
        while True:
            username=input("Enter Username:...")
            if userExists(username)==1:
                print("User already exists...Try another username..")
            else:
                break
        while True:
            password=input("Enter Passwrod...")
            val=passwordValidation(password)
            if val==True:
                fhand.write(username)
                fhand.write("  ")
                fhand.write(password)
                fhand.write('\n')
                print("User Added successfully...Now you can proceed to login..")
                break
            else:
                print("Try Again...")
    if choice==2:
        fhand=open("Password.txt","r")
        username=input("Enter the Username...")
        for line in fhand:
            line=line.rstrip()
            words=line.split()
            if username in words:
                password=input("Enter the password")
                if password in words:
                    print("Signed-in")
                    break
                else:
                    print("Wrong password...Try again")
        break


choice=int(input(
"""Enter 1 to Add new username and password
Enter 2 to Sign-in
Enter 0 to clear database
Enter 99 to Quit..."""))
