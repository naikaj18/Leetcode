# nums = [0,1,2,2,3,0,4,2]
# val = 2
# occ = 0
# og = len(nums)-1
# loop = len(nums)-1
# for i in range(0,loop):

#     if i>loop:
#         break
#     if nums[i] == val:
#         nums.pop(i)
#         loop-=1
#         i=i-1
#         occ+=1
#         # print(occ)
# for num in nums:
#     print(num)
        
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# reader = 0
# writer = 0
# n = len(nums)
# while reader < n:
#     if nums[reader] == val:
#         reader += 1
#     else:
#         nums[writer] = nums[reader]
#         reader += 1
#         writer += 1
# print(nums[writer])
# while val in nums: nums.remove(val)
# print(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2

i = 0
for j in range(len(nums)):
    if nums[j] != val:
        nums[i] = nums[j]
        i += 1

nums = nums[:i]
print(nums)
