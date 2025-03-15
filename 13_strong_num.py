# strong num == digits factorial sum == the num
# 145 = 1! + 4! + 5!

def factorials(a):
    f=1
    while(a>0):
        f=f*a
        a-=1
    return f;

n=int(input("Enter the Number::"))
m=n
sum=0
while(n>0):
    r=n%10
    fac=factorials(r)
    sum=sum+fac             # sum += factorials(r)

n=n//10
if(sum==m):
    print("{} is a palindrome".format(m))
else:
    print("{} is not palindrome".format(m))    