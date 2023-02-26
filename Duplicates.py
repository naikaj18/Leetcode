nums = [1,1,3,2,5,6,6]

# # 1. Brute force approach
# result = False
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]==nums[j]:
#             result = True #True if contains duplicate
# print(result)

# 2.Using sort
# nums.sort()
# result=False
# for i in range(1,len(nums)):
#     if nums[i]==nums[i-1]:
#         result=True
# result=False
# print(result)

#Using sets
len_nums = len(nums)
print(len_nums)
nums = set(nums)
print(len(nums))
if len(nums)==len_nums:
    print('No dupes')
else:
    print('dupes')

