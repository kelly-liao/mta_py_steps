# 練習5			提示
# 444444444		*********
#  3333333 		 ******* 
#   22222  		  *****  
#    111   		   ***   
#     0    		    *    
#    111   		   ***  
#   22222  		  *****  
#  3333333 		 ******* 
# 444444444		*********


for i in range(-4,4+1):
    for j in range(-4,4+1):
        if(abs(i)>abs(j)-1):
            print(abs(i),end='')
        else:
            print(' ',end='')
    print()
print()

for i in range(-4,4+1):
    for j in range(-4,4+1):
        if(abs(i)>abs(j)-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()