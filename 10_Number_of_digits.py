a=int(input("Enter the Number::"))
l=len(str(a))
print("There are {} digits in the given Number".format(l))
c=0
while(a>0):
    r=a%10
    c=c+1
    a=a//10
print("There are {} digits in the given number".format(c))    
