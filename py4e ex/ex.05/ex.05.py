x = input('Enter Hours: ')
y = input('Enter Rate: ')
try:
    fx = float(x)
    fy = float(y)
except:
    print ("Error, please enter numeric input")
    quit()
print (fx, fy)
if fx > 40 :
    reg = fx * fy
    otp = (fx - 40.0) * (fy * 0.5)
    xy = reg + otp
else:
    xy = fx*fy
print ("Pay:",xy)
