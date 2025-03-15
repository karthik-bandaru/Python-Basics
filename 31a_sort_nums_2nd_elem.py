# input = [(1,2),(3,1),(5,4)]
# output = [(3,1),(1,2),(5,4)]
a = [(1,2),(3,1),(5,4)]
n = len(a)
for i in range(n):
    min = i
    for j in range(i+1,n):
        if a[j][1] < a[min][1]:
            min = j
    a[i],a[min] = a[min],a[i]
print(a)

a.sort(key = lambda x : x[1])
print(a)
