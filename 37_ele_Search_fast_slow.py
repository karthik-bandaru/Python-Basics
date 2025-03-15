def slow_fast_search(arr, target):
    slow = 0
    fast = 0
    n = len(arr)
    k = 0 
    while slow < n or fast < n:
        if (slow <n and arr[slow] == target) or (fast < n and arr[fast] == target):
            return True
        k+=1
        slow += 1
        fast += 2
        if (fast < n and arr[fast] > target) or (arr[n-1] < target):
            break
    return k,False

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 20

print(slow_fast_search(arr, target))