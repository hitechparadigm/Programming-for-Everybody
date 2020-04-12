# Assignment 10.2 - Programming for Everybody, Python Data Structures, Week 6
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
counts = dict()
for line in fhand:
    if not line.startswith('From '): continue
    line = line.split()
    line = line[5]
    line = line.split(':')
    line = line[0]
    counts[line] = counts.get(line, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)
lst = sorted(lst)
for key, val in lst:
    print(key, val)
