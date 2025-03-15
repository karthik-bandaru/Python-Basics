arr = [3,4,5,8,9]
n = len(arr)
count = 0
for i in range(n):
    if arr[0] <= arr[i]:
        count += 1
print("Output : ",count)