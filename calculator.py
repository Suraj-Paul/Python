print("Program using global varialble,"'\n')
def hscreen():
    print("1.ADD",'\n')
    print("2.SUBTRACT", '\n')
    print("3.MULTIPLY", '\n')
    print("4.QUIT", '\n')
def menu():
    return eval(input("Enter your choice (1/2/3/4)"))
result=0.0
arg1=0.0
arg2=0.0
def getinput():
    global arg1,arg2
    arg1=float(input("Enter first number"))
    arg2=float(input("Enter second number"))
def report():
    print(result)
def add():
    global result
    result=arg1+arg2
def sub():
    global result
    result=arg1-arg2
def mul():
    global result
    result=arg1*arg2
def div():
    global result
    result=arg1/arg2
def main():
    done=False
    while not done:
        hscreen()
        choice=menu()
        if choice==1:
            getinput()
            add()
            report()
        elif choice==2:
            getinput()
            sub()
            report()
        elif choice==3:
            getinput()
            mul()
            report()
        elif choice==4:
            getinput()
            div()
            report()
        else:
            done=True
main()


