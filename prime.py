#prime number code.
n=eval(input("Enter any number to cheak it is prime or not"))
if (n>1):
    for i in range (2,n//2):
        if(n%i==0):
            print(n,"is not a prime number")
            break
    else:
            print(n,"is a prime number")
else:
    print(n,"is not a prime number")





