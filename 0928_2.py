# 練習2
# 1
# 01
# 101
# 0101
# 10101

for i in range(1,5+1):
    for j in range(1,i+1):
        if(i%2 == 0):
            print((j+1)%2,end=' ')
        else:
            print(j%2,end=' ')
    print()

# boolean=0
# for j in range(1,6):
#     for i in range(1,j+1):
#         boolean=boolean+1
#         if boolean%2==0:
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()
