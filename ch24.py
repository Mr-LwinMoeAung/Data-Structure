print(' *** Alphabet Sequence (A-Z) ***')         
user=input('Enter character step length : ')      
alpha,step,length=user.split()                    
ans=0                                             
step=int(step)                                      
length=int(length)                                 
x=ord(alpha)                                       
if x<91:                                          
    for i in range(0,length*step,step):            
        ans=x+i                                    
        while ans>90:                              
            x=x-26                                  
            ans=ans-26                  
        print(chr(ans),end='')                   
        if i<(length*step)-step:                
            print('=',end='')                       
    print()                                        
else:                                               
    print('Invalid input !!!')                     
print('===== End of program =====')    