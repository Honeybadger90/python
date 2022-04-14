largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        xnum = float(num)
    except:
        print('Invalid input')
        continue

    if largest is None :
        largest = xnum
    elif xnum > largest :
        largest = xnum
    #print(largest, xnum)

    if smallest is None :
        smallest = xnum
    elif xnum < smallest :
        smallest = xnum
    #print(smallest, xnum)

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
