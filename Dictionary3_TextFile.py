#Counting the words in an Input line
counts=dict()
fhand=open("Text.txt")
for line in fhand:
    line=line.rstrip()
    words=line.split()
    print("Counting...")
    for word in words:
        counts[word]=counts.get(word,0)+1
print("Counts ",counts)
