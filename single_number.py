
# # Using XOR to eliminate duplicate pairs in the list.
# nums = [1,1,2,3,3,4,4]
# result = 0
# for num in nums:
#     result ^= num
# print(result)

# from collections import defaultdict  #Using dictionary

# nums = [1,1,2,3,3,4,4]
# hash_table = defaultdict(int)
# for i in nums:
#     hash_table[i] += 1
        
# for i in hash_table:
#     if hash_table[i] == 1:
#         print(i)

#Using dict2
# nums = [1,1,2,2,3,3,4,4,5]
# hash_table ={}
# for num in nums:
#     if num in hash_table:
#         hash_table[num]+=1
#     else:
#         hash_table[num]=1
# #print(hash_table)
# for num in hash_table:
#     if hash_table[num]==1:
#         print(num)

#Using math
nums = [1,1,2,2,3,3,4,4,5]
sum =0
sum1 =0
for num in nums:
    sum+=num

for num in set(nums):
    sum1 += num

result =  2*sum1 - sum
print(result)