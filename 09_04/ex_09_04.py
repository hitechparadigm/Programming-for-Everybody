# Assignment 9.4
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
email_d = dict()
for line in fh:
    if not line.startswith('From '): continue
    line = line.split()
    line = line[1]
    email_d[line] = email_d.get(line,0) + 1
bigcount = None
bigword = None
for word,count in email_d.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
# The End
