string = "aabbcc";  
flag = 0 
for i in range(0, len(string)):  
    count = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;  
            string = string[:j] + '0' + string[j+1:];    
    if(count > 2 and string[i] != '0'):  
        flag+=1;
        
        print(string[i],':',count)
if flag>=1:
	print('Not a Sherlock string')
else:
	print('sherlock string') 