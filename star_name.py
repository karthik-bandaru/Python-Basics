a = "PYTHON"
n = len(a)
for i in range(n):
    for j in range(i+1):
        print(a[j],end=" ")  
    print()   
for i in range(n):
    for j in range(n-i-1):
        print(a[j],end=" ") 
    print()         