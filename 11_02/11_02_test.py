import re
hand = open('textfile.txt')
for line in hand:
    line=line.rstrip()
    x=re.findall('\S+?@\S+',line)
    print(x)
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)


import re
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
counts = dict()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('^From (\S+@\S+)',line)
    if len(stuff) != 1: continue
    print(stuff)
