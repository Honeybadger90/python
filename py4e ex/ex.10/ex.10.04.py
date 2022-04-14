fname = input("Enter file name: ")

fh = open(fname)
count = 0
total = 0
countav = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    num = float(line[21:])
    total = num + total

countav = total / count

print("Average spam confidence:", countav)
