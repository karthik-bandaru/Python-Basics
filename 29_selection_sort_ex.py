# arr=[1,10,7,15,6,9,4]
# def selection_sort(arr):
#     n = len(arr)
    
#     for i in range(n):
#         minimum = i
#         for j in range(i+1,n):
#             if arr[j] < arr[minimum]:
#                 minimum = j
                
#         arr[i] , arr[minimum] = arr[minimum] , arr[i]    
    
    
#     return arr;

# print(selection_sort(arr)) 













# arr=[1,10,7,15,6,9,4]

arr = [1,4,6,7,9,10,15]
def selection_sort(arr):
    n = len(arr)
    check = True
    for i in range(n):
        minimum = i
        for j in range(i+1,n):
            if arr[j] < arr[minimum]:
                minimum = j
                check = False
        arr[i] , arr[minimum] = arr[minimum] , arr[i]    
    
    if check:
        return "Given Array Is already sorted..."
    
    return arr;

print(selection_sort(arr))        