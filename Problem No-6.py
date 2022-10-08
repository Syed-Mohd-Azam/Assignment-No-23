# Create a generator to produce first n prime numbers.
def prime(n):
    i,count=2,0
    while(count<=4):
        for e in  range(2,i,1):
            if i%e==0:
                break
        else:
            yield i
            count=count+1
        i=i+1
for e in prime(int(input("Enter the value of n to generate first n prime numbers: "))):
    print(e,end=" ")