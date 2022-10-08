# Create a generator to produce first n odd natural numbers.
def odd_natural(n):
    i=0
    while(i<n):
        yield (2*i+1)
        i=i+1
for e in odd_natural(int(input("Enter the value of n to generate first n odd natural numbers: "))):
    print(e,end=" ")