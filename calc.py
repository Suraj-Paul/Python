from math import sqrt
def is_prime(n):
    tf=2
    rt=n-1
    while tf<=rt:
        if n%tf==0:
            return False
        else:
            return True
    tf+=1
def fact(n):
    i = 1
    fact = 1
    if n == 0:
        print("factorial =", fact)
    else:
        while i <= n:
            fact = fact * i
            i += 1
        return fact;



num=eval(input("Enter a number to check it is prime or not:"))

a=is_prime(num)
print(a)
'''f= eval(input("Enter any number to find its factorial:"))
a=fact(f)
print(a)'''