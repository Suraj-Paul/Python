from math import*
a,b,c=eval(input("enter three values for a,b,c"))
d=b*b-4*a*c
if d>0:
   x1=(-b+sqrt(d))/2*a
   x2=(-b-sqrt(d))/2*a
   print("root's of quadratic equation is",x1,x2)
elif d==0:
    x=-b/2*a
    print("Ans =",x)
