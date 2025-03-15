

def search_insert( nums: list[int], target: int) -> int :
    s = 0
    e = len(nums)

    while s < e :
        mid = (s + e) // 2
        if target > nums[mid]:
            s = mid + 1 
        else:
            e = mid
    return s

nums_arr = [1,3,3,5,7,8] 
target = 7
print(search_insert(nums_arr,target)) 

##

def searchInsert(nums,target):
    left = 0
    right = len(nums)

    while left < right :
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left
print(searchInsert(nums_arr,target))



## This is the Correct Code...!!


def Insert(arr, target):
    
    s = 0
    e = len(arr) - 1
    res = -1 

    while(s<=e):
        mid = (s+e)//2
        if(arr[mid] == target):
            res = mid
            e = mid - 1

        elif(target > arr[mid]):
            s = mid + 1
        else:
            e = mid - 1
    
    return res if(res!=-1) else s

print(Insert(nums_arr,3))

        