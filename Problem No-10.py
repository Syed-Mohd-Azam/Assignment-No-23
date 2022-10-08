# Define a function which calculates HCF of two numbers. Define and apply a decorator to check whether two given numbers are co-prime or not.
def decorator(HCF):
    def coprime(a,b):
        f1,f2=[],[]
        for e in range(1,a+1,1):
            if a%e==0:
                f1.append(e)
            else:
                continue
        for e in range(1,b+1,1):
            if b%e==0:
                f2.append(e)
            else:
                continue
        s1,s2=set(f1),set(f2)
        if s1.intersection(s2)==set([1]):
            print ("Given numbers are coprime! ")
        else:
            print("Numbers are not coprime! ")
        HCF(a,b)
    return(coprime)
@decorator
def HCF(a,b):
    hcf,factors1,factors2=1,[],[]
    while(a>1):
        for e in range(2,a+1,1):
            if a%e==0:
                factors1.append(e)
                a=int(a//e)
                break
            else:
                continue
    while(b>1):
        for e in range(2,b+1,1):
            if b%e==0:
                factors2.append(e)
                b=int(b//e)
                break
            else:
                continue
    for e in factors1:
        for k in factors2:
            if e==k:
                hcf=hcf*k
                factors2.remove(k)
                break
            else:
                continue
        continue
    print("HCF between two numbers is : ",hcf)
HCF(int(input("Enter first number : ")),int(input("Enter second number: ")))