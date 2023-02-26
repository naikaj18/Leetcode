# # # nums = [1,2,2,3,4,5]
# # # val = 2
# # # num=0
# # # for num in nums:
# # #     print(num)
# # #     if(nums[num]==val):
# # #         nums.remove(num)
        
# # # for num in nums:
# # #     print(num)
        
# # nums=[9,4,6,3,2,5,2,1]
# # val=1
# # n=len(nums)
# # for i in range(0,n-1):
# #     if(nums[i]==val):
# #         nums.pop()
# #         n-=1
# # print(nums)

# nums = [3,2,2,3]
# val = 3
# nums = [num for num in nums if num!=val]
# print(len(nums))
# print(nums)

nums=[3,2,2,2,4,5]
val=2
i = 0
for j in range(len(nums)):
    if nums[j] != val:
        nums[i] = nums[j]
        i += 1
print(nums)
print(i)
