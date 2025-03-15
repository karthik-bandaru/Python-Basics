arr = [9,7,15,2,8,12,1]

# sorting techniques 

# so many sorting techniques...

# three tectechniques.....

# selection sorting 

# bubble sorting 

# insertion sorting.... 

# etc 

def selection_sorting(arr):
    n = len(arr)
    for i in range(n):
        minimum = i 
        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i],arr[minimum] = arr[minimum], arr[i]
        
        print("arr", arr)
    return arr 

print(selection_sorting(arr))









def selection_sorting(arr):
    n = len(arr)
    flag = True
    for i in range(n):
        minimum = i 
        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                minimum = j
                flag = False
        arr[i],arr[minimum] = arr[minimum], arr[i]
            
        #print("arr", arr)
    
    if flag:
        return "Already sorted selection"
        
    return arr 

print(selection_sorting(arr))


arr = [9,7,15,2,8,12,1]

def selction_sorting(arr):
    n = len(arr)

    for i in range(n):

        minimum = i

        for j in range(i+1,n):
            if arr[j] < arr[minimum]:
                minimum = j 

        arr[i],arr[minimum] = arr[minimum],arr[i]

    return arr
print(selction_sorting(arr))            
    







































