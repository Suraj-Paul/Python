from calc import*
def main():
    num=int(input("Enter any number"))
    if is_prime(num):
        print("It is a prime number")
    else:
        print("It is not a prime number")

num1=eval(input("Enter a number to find factorial"))
f=fact(num1)
print("Factorial",f)
main()
