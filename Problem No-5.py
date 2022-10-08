# Create a generator to produce first n terms of Fibonacci series.
def fibonacci(n):
    a,b,i=0,1,n-2
    yield a
    yield b
    while(i>0):
        yield a+b
        a,b=b,a+b
        i=i-1
for e in fibonacci(int(input("Enter the value of n to generate n terms of fibonacci series : "))):
    print(e,end=" ")