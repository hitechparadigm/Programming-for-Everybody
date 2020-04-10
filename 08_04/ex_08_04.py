fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lst2 = list()
for line in fh:
    linelst = line.split()
    for i in linelst:
        if i not in lst2:
            lst2.append(i)
lst2.sort()
print(lst2)
