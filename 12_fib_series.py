# n=int(input("Enter the NUmberrr:"))
# a=0
# b=1
# ct=0
# print(a,end=" ")
# print(b,end=" ")
# while(ct<=n-3):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
#     ct=ct+1
    
# n = int(input("Enter Number of series u want : "))
# a = int(input("Enter 1st Number : "))
# b = int(input("Enter 2nd Number : "))
# while(n>0):
#     print(a,end = " ")
#     c = a + b
#     a = b 
#     b = c 
#     n -= 1

n = int(input("Enter number series : "))
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
def fib_series(n,a,b):
    fib = [a,b]
    for i in range(2,n):
        nxt_num = fib[i-1] + fib[i-2]
        fib.append(nxt_num)
    return fib

print(fib_series(n,a,b))    
    