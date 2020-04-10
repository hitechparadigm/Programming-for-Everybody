# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total_piece = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        count = count + 1
        sindex = line.find(':')
        piece = line[sindex+1:]
        piece = float(piece)
        total_piece = total_piece + piece
print("Average spam confidence:", (total_piece/count))

# Assignment 7.2 is complete
