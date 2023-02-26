def demo():
    S = [1,20,10,2]
    x = 20

    # for i in range(len(S)):
    #     for j in range(i+1,len(S)):
    #         if S[i]*S[j]==x:
    #             return S[i], S[j]
    i=0
    j=1
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            if((S[i]*S[j])==x):
                return S[i],S[j]
            


               

# print(demo())
print(demo())


