arr = [1,2,3,5]
def missing_ele(arr):
    l = len(arr)
    for i in range(l):
        if(arr[i]!=i+1):
            arr.insert(i,i+1)
            return arr
print(missing_ele(arr))      
# arr.insert(3,4)
# print(arr)