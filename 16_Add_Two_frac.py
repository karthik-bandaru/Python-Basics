a=int(input("Enter the Number a::"))
b=int(input("Enter the Number b::"))
c=int(input("Enter the Number c::"))
d=int(input("Enter the Number d::"))
print("Your Fraction isss {}/{} and {}/{}".format(a,b,c,d))
print("The addition of Two fractions iss::",end=" ")

N=(a*d)+(b*c)
D=(b*c)
print("{}/{}".format(N,D))

# def gcd(x,y):
#     while y!=0:
#         r = x % y
#         x = y
#         y = r
#     return x

def gcd(head,side):
    while(side):
        r = head % side
        head = side
        side = r
    return head    
    

cmnd = gcd(N,D)
print(cmnd)
N //= cmnd
D //= cmnd
print("The addition of Two fractions iss::",end=" ")
print("{}/{}".format(N,D))