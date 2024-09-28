# 練習1
# AAAAA
# BBBB
# CCC
# DD
# E
list1=['A','B','C','D','E']
for i in range(1,5+1):
    for j in range(6-i,0,-1):
        # print(chr(64+i),end='')
        print(list1[i-1],end='')
    print()
    