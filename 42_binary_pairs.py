#  arr = [0,1,0,1,1]

# index(0,3) = (0,1)
# index(0,4) = (0,1)
# index(1,3) = (0,1)
# index(1,4) = (0,1)
# index(2,3) = (0,1)
# index(2,4) = (0,1)

arr = [0,0,0,1,1]
l = len(arr)
c = 0
for i in range(l):
    if (arr[i] == 0):
        for j in range(i+1,l):
            if (arr[j] == 1):
                c += 1
print("Ans : ",c)               
