# Create a generator to produce first n even natural numbers.
def even_natural(n):
    i=1
    while(i<=n):
        yield (2*i)
        i=i+1
for e in even_natural(int(input("Enter the value of n to generate first n even natural numbers: "))):
    print(e,end=" ")