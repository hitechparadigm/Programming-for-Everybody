# Assignment 9.4
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
email_d = dict()
for line in fh:
    if not line.startswith('From '): continue
    #if len(line) < 3 : continue - guardian
    # transforming lines to list
    line = line.split()
    # reading values #1 from list
    line = line[1] # I have string values
    # create list with email addresses only
    #linelist = linelist.split()
    # print(linelist) - checking if I have list of emails
    #for i in linelist:
    email_d[line] = email_d.get(line,0) + 1

#print(email_d) - checking dictionary
bigcount = None
bigword = None
for word,count in email_d.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
# The End
