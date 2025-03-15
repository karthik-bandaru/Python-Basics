import math 
n=int(input("Enter The Number::"))
print("The Factors of a Given number is ::",end=" ")
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")
print()        

res=[]

print(int(math.sqrt(28)))
for i in range(1,int(math.sqrt(n))+1):
    if n % i == 0:                      ## n%i==0 and i*i == n
        if int(math.sqrt(n)) == i:             # res.append(i)
            res.append(i)
        else:
            res.append(i)
            res.append(n//i)
            
res.sort()
print(res)