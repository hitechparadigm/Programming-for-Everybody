fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#print(counts)

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
#print(lst)
lst = sorted(lst, reverse=True)
#print(lst)
#print(sorted([(v,k) for k,v in counts.items()], reverse=True))
for val, key in lst[:10]:
    print(key, val)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])
