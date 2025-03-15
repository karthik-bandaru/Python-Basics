arr = [1,2,2,2,2,3,1,1]
m = max(set(arr), key = arr.count)    ## key = arr.count()  X X X 
print(max(arr))
print(m)
print(set(arr))