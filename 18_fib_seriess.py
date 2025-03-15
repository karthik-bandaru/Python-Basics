n=int(input("Enter Number of series U want::"))
# first=-3
# second=-2
# print(first,end=" ")
# print(second,end=" ")

def fib_series(first, second):

    res = [first, second]

    for i in range(n-2):
        third = res[-1]+ res[-2]
        res.append(third)
        # first, second = second, third 
        # first = second
        # second = third

    return res 

a = int(input())
b = int(input())

print(fib_series(a, b))