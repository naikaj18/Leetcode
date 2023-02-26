nums = [3,2,2,3]
val = 2
i=0
count=0
while i<len(nums):
    if nums[i]==val:
        nums.pop(i)
print(nums)