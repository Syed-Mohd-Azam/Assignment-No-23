# Create an endless iterator using generator method to produce Prime numbers.
def prime():
    i=3
    while True:
        for e in range(2,i,1):
            if i%e ==0:
                break
        else:
            yield i 
        i=i+1
it=prime()
print("First prime number is : ",2)
while True:
    n=int(input("Enter (0) to stop / enter (1) to print next prime number: "))
    if n==0:
        exit()
    else:
        print("Next prime number is : ",next(it))