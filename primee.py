import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        
        if n % i == 0:
            return False 
            
    return True
        

res = [i for i in range(2,51) if isPrime(i) ]
print(res)

for i in range(2, 51):
    if isPrime(i):
        print(i)
        
