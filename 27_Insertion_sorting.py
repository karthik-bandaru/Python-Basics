arr = [9,7,15,2,8,12,1]


def insertion_sorting(arr):
    n = len(arr)
    
    for i in range(1, n):
        
        j = i 
        
        while arr[j-1] > arr[j] and j>0 :
            arr[j], arr[j-1] = arr[j-1], arr[j]
            print(arr,"\n\n")
            
            j -= 1 
            
    return arr 
    
print(insertion_sorting(arr))