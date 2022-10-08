"""Define a function which takes lengths of three sides of a triangle as arguments and display the perimeter or triangle.
Define and apply a decorator which checks for the validity of the triangle on the basis of lengths of the side.
This makes the perimeter to be displayed when the triangle can exist with the given lengths of the sides."""
def decor(perimeter_triangle):
    def validity(a,b,c):
        if a+b>c and a+c>b and b+c>a:
            print("Triangle is valid with these three sides!")
            perimeter_triangle(a,b,c)
        else:
            print("Triangle is not valid with these sides! ")
    return(validity)
@decor
def perimeter_triangle(a,b,c):
    print("The perimeter is : ",(a+b+c))
perimeter_triangle(int(input("Enter first side: ")),int(input("Enter second side: ")),int(input("Enter third side: ")))