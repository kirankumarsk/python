#A program to find a read through a Text file and counting the number of words and lines
#This will also return the histogram of the words and its frequency in the given content
import os
os.system('cls')
import WelcomeMsg
def callFile():
    try:
        fhand=open(input("Enter the FILE name..."))
        print("File read SUCCESSFULLY")
    except:
        temp=input("INVALID file NAME!!\nHit ENTER to re-enter the FILE name\nHit 'q' to Quit program")
        if(temp=='q'):
            quit()
        callFile()
    return fhand

#CODE FOR COUNTING THE NUMBER OF LINES AND WORDS IN THE GIVEN FILE
counts=dict()
fhand=callFile()
lineCounter=0
wordCounter=0
for line in fhand:
    line=line.rstrip()
    words=line.split()
    lineCounter+=1
    for word in words:
        wordCounter+=1
        counts[word]=counts.get(word,0)+1
print(f"There are total {lineCounter} lines and {wordCounter} words in the Given File")

#Code to create a tupple and use its properties for sorting of the list
#Now there are two methods to do the same
#Method-1
print("Hit Enter to See the Histogram...")
sortedList=list()
for key,value in counts.items():
    sortedList.append((value,key))
sortedList=sorted(sortedList,reverse=True)
print(sortedList)

#Method 2: One Line code using tuples
os.system('cls')
input("Hit Enter to see the one line code")
print(sorted([(value,key) for key,value in counts.items()],reverse=True))
