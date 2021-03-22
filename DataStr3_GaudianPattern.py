#This program demonstrates how to same your code from
#blowing up...
fhand=open("Resume.txt")
for line in fhand:
    line=line.rstrip()
    words=line.split()
    #Garurdian pattern-1
    if line=='':
        continue
    #Garurdian pattern-2
    if len(words)<3:
        continue
    print("Words: ",words)
    if words[0]!='-':
        continue
    print(words[2])
