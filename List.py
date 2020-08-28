'''lst=['ram','mohan','rohit','varun','divya','priti',24,64,86,2.40,0.09]
lst[5]='ram'
print(lst)

#Enter two numbers to swap it.
def swap(a,b):
    x = a
    a = b
    b = x
    print("a=", a)
    print("b=", b)
m,n=eval(input("Enter two number to swap it."))
j=swap(m,n)
print(j)'''

#searching and sorting.
def make_lst(n):
    import random
    result=[]
    for i in range(n):
        rand=random.randrange(100)
        result+=[rand]
    return result
def selsort(lst):
    n=len(lst)
    for i in range(n-1):
        small=i
        for j in range(i+1,n):
            if lst [j]<lst[small]:
                small=j
            if i!=small:
                lst[i],lst[small]=lst[small],lst[i]
def bubblesort(lst):
    n=len(lst)
    for i in range(n-1):
        small=i
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
def bsearch(i,lst,lo,hi):
    m=0
    m=int((lo+hi)/2)
    if i==lst[m]:
        return m
    elif i>=lst[m]:
        return bsearch(i,lst,m+1,hi)
    else:
        return bsearch(i,lst,lo,m-1)
def quick_sort(lst,l,h):
    if l<h:
        q=partition(lst,l,h)
        quick_sort(lst,l,q-1)
        quick_sort(lst,q+1,h)
def partition(lst,l,h):
    x=lst[h]
    i=l-1
    for j in range(l,h):
        if lst[j]<x:
            i+=1
            lst[i],lst[j]=lst[j],lst[i]
    lst[i+1],lst[h]=lst[h],lst[i+1]
    return i+1
def main():
    l=0
    p=0
    num=int(input("How many numbers you want to sort?:"))
    ele=make_lst(num)
    print("The element are :",ele)

    selsort(ele)
    print("The sorted elements by using selection sort are:",ele)

    bubblesort(ele)
    print("The sorted elements by using bubble sort are   :",ele)

    r = len(ele) - 1
    quick_sort(ele, p, r)
    print("The sorted elements by using quick sort are    :",ele)

    item=int(input("Enter an element to search in the list:"))
    h=len(ele)-1
    p=bsearch(item,ele,l,h)
    print("The element is found at position :",p)

main()

