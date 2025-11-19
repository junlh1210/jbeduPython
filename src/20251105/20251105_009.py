x=int(input("점수 :  "))

if (x>=0 and x<=59):
    print("F")
elif (x>=60 and x<=69):     
    print("D")
elif (x>=70 and x<=79):
    print("C")
elif (x>=80 and x<=89):
    print("B")
else:
    print("A")