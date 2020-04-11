# Dictionaries and Files
counts = dict()

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    #line = line.rstrip()
    list1 = line.split()
    for i in list1:
        counts[i] = counts.get(i,0) + 1

print('Counts', counts)
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
