#Histogram
counts=dict()
fhand=open('Resume.txt')
for line in fhand:
    line=line.split()
    for name in line:
        counts[name]=counts.get(name,0)+1
print(counts)
