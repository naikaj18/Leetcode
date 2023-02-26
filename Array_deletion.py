nums = [0,0,1,1,1,2,2,3,3,4]

Length = len(nums)
print(Length)
for i in range(Length-2,-1,-1):
    if nums[i]==nums[i+1]:
        for j in range(i+1,Length):
            nums[j-1]=nums[j]
        Length-=1
print(Length)
print(nums[:Length])