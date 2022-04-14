def computepay(h, r):
    hrs = float(h)
    rx = float(r)
    if hrs > 40 :
        ro = float(hrs - 40) * float(rx * 0.5)
        pxy = (rx * hrs)+ ro
    else:
        pxy = float(h) * float (r)
    return pxy



h = input("Enter Hours:")
r = input("Enter Rate")
p = computepay(h, r)
print("Pay", p)
