# Create a generator to produce squares of first N natural numbers.
def squares(n):
    i=1
    while(i<=n):
        yield(i*i)
        i=i+1
for e in squares(int(input("Enter the value of n to generate the squares of first n natural numbers: "))):
    print(e,end=" ")