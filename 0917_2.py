# 練習2
# A
# BB
# CCC
# DDDD
# EEEEE

#hint: A的ascii code是65
for i in range(1,6):
    # print(i)
    for j in range(i):
        print('%c'%(64+i),end='')
    print()