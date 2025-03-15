
a = int(input("Enter the 1st elem:: "))
b = int(input("Enter the 2nd elem:: "))
f = int(input("Enter required digit in series:: "))

def fib(first,second):
    res = [first,second]
    for i in range(f-2):               # range(2,n)   
        third = res[-1] + res[-2]      # third = first + second
        res.append(third)          # res.append(third)   first, second = second, third      
    return res[f-1]                # BCZ IN array that last index value is (f-1) only       

print("Ans : ",fib(a,b))