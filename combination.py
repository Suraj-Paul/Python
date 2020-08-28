def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

m=eval(input("Enter value of n"))
r=eval(input("Enter vlue of r"))
ncr=fact(m)/fact(r)*fact(m-r)
print(ncr)