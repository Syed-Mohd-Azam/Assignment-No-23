# Create an endless iterator using generator method to produce terms of Fibonacci series.
def fibonacci():
    a,b=0,1
    yield a 
    yield b 
    while True:
        yield a+b
        a,b=b,a+b
it,l1=fibonacci(),[]
while(True):
    n=int(input("Enter (1 or 0) to store more elements of fibonacci series /to stop here : "))
    if n==0:
        break
    else:
        l1.append(next(it))
for e in l1:
    print(e,end=" ")      