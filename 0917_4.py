# 練習4
# 01111
# 20222
# 33033
# 44404
# 55550

for i in range(1,6):
    for j in range(1,6):
        if i == j:
            print('0',end='')
        else:
            print(i,end='')
    print()