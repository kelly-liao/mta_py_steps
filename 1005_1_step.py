# a = int(input("give me a number:"))
# b = abs(a)
# print('abs %d is %d'%(a,b))

for i in range(-4,5):
    c = abs(i)
    print(c,end=' ')
print()

for i in range(-3,4):
    c = abs(i)
    print(c*' ',end='')
    for j in range(1,4-c+1):
        print('* ',end='')
    print()