arr = [7, 11, 25, 2, 2, 5, 30, 3, 9, 39, 6, 42, 66, 55, 29, 100]
arr.sort()
print(arr)
target = 100

def binary_search(arr, target):
    s = 0 
    e = len(arr)-1

    while s < e:
        mid = (s+e)//2 
        

        if target > arr[mid]:
            s = mid + 1

        else:
            e = mid
    
    if arr[s] == target:
        print("{} is the position of {}".format(s,target))
        return True 
    return False

print(binary_search(arr, target))


##THis is wrong because 5 is present at mainly at 4th index but it prints 5th indexx
#so actually we search from the first index whenever we found that then simultaniously it prints first index..
l = [2,2,3,3,5,5,6,6,7,8,9]
l.sort()
target_el = 2

def binary_search_function(l, target_el):
    low = 0
    high = len(l)-1
    res = -1 
    while low <= high:
        mid = (low + high)//2 
        if l[mid] == target_el:
            # print("{} is present at {}".format(target_el,mid))
            # return "element is present"
            res = mid
            high = mid - 1
        elif target_el > l[mid]:
            low = mid + 1 
        else:
            high = mid - 1 
    if res != -1:
        return "Element is Present @",res," Position"
    else:
        return ("There is no Element..!")

res = binary_search_function(l, target_el)
print(res)