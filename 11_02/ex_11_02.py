# Assignment 11.2 - Programming for Everybody, Python Data Structures, Week 6

import re
fhand = open('regex_sum_109878.txt')
sum = 0
#count = 0
lst2 = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)',line)
    lst2 = lst2 + stuff
for i in lst2:
    #count = count+1
    sum = sum + int(i)
#print(count)
print(sum)
