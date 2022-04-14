x = input('Enter Hours: ')
y = input('Enter Rate: ')
fx = float(x)
fy = float(y)
#print (fx, fy)
if fx > 40 :
    #print("Overtime")
    reg = fx * fy
    otp = (fx - 40.0) * (fy * 0.5)
    #print (reg,otp)
    xy = reg + otp
else:
    #print("Regular")
    xy = fx*fy
print ("Pay:",xy)
