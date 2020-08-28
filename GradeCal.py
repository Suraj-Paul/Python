m1,m2,m3,m4,m5=eval(input("Enter marks student"))
avg=(m1+m2+m3+m4+m5)/5
if avg>90 and avg<=100:
    print("O grade")
elif avg>80 and avg <=90:
    print("E grade")
elif avg>70 and avg<=80:
    print ("A grade")
elif avg>60 and avg<=70:
    print("B grade")
elif avg>50 and avg<=60:
    print("C grade")
else:
    print("Fail")