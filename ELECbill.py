unit=eval(input("Enter the energy consumed in unit"))
if unit<=200:
    rate=unit*0.5
    print("Rate per unit =",rate)
elif unit>=201 and unit<=400:
    rate=100+0.65*(unit-200)
    print("Rate per unit=",rate)
elif unit>=401 and unit<=600:
    rate=230+0.80*(unit-400)
    print("Rate per unit =",rate)
elif unit>600:
    rate=425+0.80*(unit-600)
    print("Rate per untit =",rate)