i=1
fact=1
n=eval(input("Enter any number to find its factorial:"))
if n==0:
    print("factorial =",fact)
else:
    while i<=n:
        fact=fact*i
        i+=1
    print("Factorial=",fact)