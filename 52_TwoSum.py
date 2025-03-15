def twoSum(nums, target):
    # res = []
    for i in nums:
        k = target - i
        if k in nums:
            return [nums.index(i),nums.index(k)]
print(twoSum([3,2,4],6))

# l = [3,3]
# if 3 in l:
#     print(l.index(3))
# print()


