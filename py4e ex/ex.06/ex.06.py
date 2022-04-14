score = input("Enter Score:")
score = float (score)
if score > 1 :
    print ("Number to high, stay inbetween 0.0 and 1.0")
if score < 0 :
    print ("Number to low, stay inbetween 0.0 and 1.0")
elif score >= 0.9 :
    print ("A")
elif score >= 0.8 :
    print ("B")
elif score >= 0.7 :
    print ("C")
elif score >= 0.6 :
    print ("D")
elif score < 0.6 :
    print ("F")
