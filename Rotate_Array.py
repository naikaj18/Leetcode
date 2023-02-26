nums = [1,2,3,4,5]
k = 2
length = len(nums)
k = k % length
nums[:length-k] = reversed(nums[:length-k])
nums[length-k:] = reversed(nums[length-k:])
nums[:] =reversed(nums[:])
print(nums)




 