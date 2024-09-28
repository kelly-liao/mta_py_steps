# 練習3
#  1
#  2  3
#  4  5  6
#  7  8  9 10
# 11 12 13 14 15

num=0
for j in range(1,6):
    for i in range(1,j+1):
        num = num+1
        if num < 10:
            print('%2d'%num, end=" ")
        else:
            print(num, end=" ")
    print()
