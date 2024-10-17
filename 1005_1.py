# 練習 4
#      4
#     3 3
#    2 2 2
#   1 1 1 1
#  0 0 0 0 0
#   1 1 1 1
#    2 2 2
#     3 3
#      4


for i in range(-4,4+1):
    print(abs(i)*' ',end='')
    for j in range(1,5-abs(i)+1):
        print(' %d'%abs(i),end='')
    print()
print()