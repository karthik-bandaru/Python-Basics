def prime(n):
    
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            return False 
    return True
   
a=int(input("Enter Startsfrom::"))
b=int(input("Enter Lastrange::")) 
res = [i for i in range(a,b+1) if(prime(i) and i % 10 == 3)]
print(res)

# for i in range(a,b+1):
#     if prime(i) and i % 10 == 3:
#         print(i)
#         if i % 10 == 3:
#             print(i)     
