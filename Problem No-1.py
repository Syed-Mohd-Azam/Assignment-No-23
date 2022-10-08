# Use iter and next method to access all the elements of a given set using while loop.
s={1,2,3,4,5,6.5,"iNeuron",True,(1,3,4,5)}
i,len,it=0,len(s),iter(s)
while(i<len):
    print(next(it),end="  ")
    i=i+1