def fun1():
    n=eval(input("Enter the number up to which you want the sum"))
    i = 1
    s = 0
    while i <= n:
        s += i
        i += 1
    print(s)
fun1()
#fun1()
def fun2():
    n=eval(input("Enter the number upto which you want to get the sum of odd intrger"))
    i = 1
    s = 0
    while i <= n:
        s += i
        i += 2
    print("Sum of odd numbers is", s)
fun2()


#sumation of numbers up to n using for loop
def sum(m):
    s=0
    for i in range(1,m+1,1):
        s=s+i
    return(s)
n=eval(input("Enter number to get the sum"))
x=sum(n)
print(x)


'''#sumation of numbers up to n using while loop
def sum(m):
    i=0
    s = 0
    while i<=m:
        s=s+i
        i+=1
    return (s)
n=eval(input("Enter number to get the sum"))
x=sum(n)
print(x)'''
#area of circle
def area(x):
    a=3.141*x*x
    return a
v=eval(input("Enter the value of radius"))
print(area(v))

#multiplicative table
def table(n):
    for i in range (1,11,1):
        t=n*i
        print(n,'*',i,'=',t)
m=eval(input("Enter number to find the table"))
x=table(m)
print(x)

'''def fib(n):
    a1=0
    a2=1
    if n==1:
        print(a1)
    elif n==2:
        print(a2)
    else:
        while n>=2:
m=eval(input("Enter a number to print the series"))
x=fib(m)
print(x)'''


#Biggest among three numbers.
def main(x,y,z):
    if x==y and x==z:
        print("All the numbers are equal")
    elif x>y and x>z:
        print("The first number is the biggest")
    elif y>z:
        print("Second number is biggest")
    else:
        print("Third number is the biggest")

n1,n2,n3=eval(input("Enter the three numbers"))
print(main(n1,n2,n3))



