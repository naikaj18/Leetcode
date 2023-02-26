pat = "HOR"
txt = "KISHORE"
m = len(pat)
n = len(txt)
# result=n-m
# print(result)
# for i in range(result):
#     for j in range(m):
#         if txt[i+j] != pat[j]:
#             break
#     if j==m:
#         print('pattern found in text at',i)
#     else:
#         print("No pattern found")
loop_variable=m+3
j=0
i=0
while(i<m):
    if(i==m):
       break
    else:
         while(j<n):
            if(j==loop_variable):
                break
            else:
                if(pat[i]==txt[j]):
                    print(j)
                    i+=1
            j+=1    

        
