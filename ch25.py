print(' *** Pyramid-XV ***')                        
user=int(input('Enter height : '))                 
adding=0                                            
a=ord('A')                                          
reversing=[]                                        
count=0                                             
new_count=3                                         
for i in range(user):                               
    for j in range((user-1)-i):                     
        print('-',end='')                           
    if  i%2!=0:                                     
        for j in range(i):                          
            print('.',end='')                       
    for z in range(i+1):                            
        if i%2!=0 or i==0:                          
            process=a+adding                        
            print(chr(process),end='')              
            process=ord('A')                    
            adding=0                            
        else:                                   
                adding+=1                           
        if i%2==0 and i!=0:                         
            count+=1                                
            process=a+adding                        
            process=chr(process)                    
            reversing.append(process)               
            if count==new_count:                    
                reversing=reversing[::-1]           
                for char in range(len(reversing)):  
                    print(reversing[char],end='')   
                new_count+=2                        
                reversing=[]                        
                count=0                             
            if ord(process)>=90:                    
                process=ord('A')                    
                adding=0                            
            else:                                   
                adding+=1                           
    if i%2==0 and i!=0:                            
        for j in range(i):                         
            print('.',end='')                       
    for j in range((user-1)-i):                     
        print('-',end='')                           
    print()                                         
print('===== End of program =====')                 