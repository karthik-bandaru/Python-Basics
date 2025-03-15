print("Enter the values of Coefficients of a Quadratic equations")
a=int(input("Enter the value of a::"))
b=int(input("Enter the value of b::"))
c=int(input("Enter the value of c::"))
d=(b**2)-(4*a*c)
d1=d**0.5
if(d<0):
    print("The roots of a given equations are Imaginary")
else:
    r1=(-b + d1)/(2*a)
    r2=(-b - d1)/(2*a)
    print("The solutions of given equation is\n root1={} and root2={}".format(r1,r2))