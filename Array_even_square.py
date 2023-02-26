arr = [1,2,3,4,5,9]
# n=len(arr)
# #print(n)
# j=0
# arr2 =[ ]*n
# print(arr2)
# i=0

# print(arr2)
# for i in range(n):
#     print(arr[i])
#     arr2[i] = arr[i]
#     print(i,'i am here')
#     #if i%2==0:
#         #arr2[i]=arr[i]*arr[i]

# print(arr2)
# for i in range(n):
#     j=0
#     if(i%2==0):
#         j=arr[i]*arr[i]
#         arr2.append(j)
#         # arr2[i]=j
#     else:
#         arr2.append(arr[i])
#         # arr2[i]=arr[i]

# print(arr2)

for i in range(len(arr)):
    if i%2==0:
        arr[i]*=arr[i]
print(arr)

        



