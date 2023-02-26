arr = [-20,8,-6,-14,0,-19,14,4]
if len(arr)==0:
    print('False')
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        print(i,j)
        if (arr[i]*2 == arr[j]):
            #print('I am here')
            print('True')
        elif (arr[i]%2==0 and arr[i]/2==arr[j] ):
            #print('I am here 2')
            print('True')
else:
    #print('I am here too')
    print('False')
        

    