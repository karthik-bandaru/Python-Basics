arr = [9,7,15,2,8,12,1]


def bubble_sorting(arr): #fix highest element at the last 
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("arr", arr)
                print()
        print(arr)         
       
        
        
    return arr 

print(bubble_sorting(arr))














arr = [9,7,15,2,8,12,1]
# arr = [1,2,7,8,9,12,15]

'''
def bubble_sorting(arr): #fix highest element at the last 
    n = len(arr)
    flag = True
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False
                # print("arr", arr)
    if flag:
        return "array is already sorted"
        
        
    return arr 

print(bubble_sorting(arr))




'''