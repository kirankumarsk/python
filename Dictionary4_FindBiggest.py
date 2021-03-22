#This program will find the word with maximum repitation
#You can also Enter a word and find its histogram
import os
os.system('cls')
import WelcomeMsg

counts=dict()
fhand=open("Text.txt")
lineCounter=0
wordCounter=0
for line in fhand:
    line=line.rstrip()
    words=line.split()
    lineCounter+=1
    for word in words:
        counts[word]=counts.get(word,0)+1

bigCount=None
bigWord=None
for word,count in counts.items():
    if bigCount is None or count>bigCount:
        bigWord=word
        bigCount=count

print("Line Counte: ",lineCounter)
print("Word Count: ",len(counts))
print(f"Word '{bigWord}' repeated max count of '{bigCount}'")

findMe=input("Enter the WORD you want to find...")
fhand=open("Text.txt")
counts=dict()
print(findMe)
for line in fhand:
    line=line.rstrip()
    words=line.split()
    for word in words:
        if word==findMe:
            counts[word]=counts.get(word,0)+1
print(findMe,"has repeated for",counts, "times")
#print(counts.keys(),"has repeated for",counts.values(), "times")
