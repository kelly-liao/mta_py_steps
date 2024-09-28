for i in range(-4,4+1):
    print(abs(i)*' ',end='')
    for j in range(1,5-abs(i)+1):
        print(' %d'%abs(i),end='')
    print()
print()

for i in range(-4,4+1):
    for j in range(-4,4+1):
        if(abs(i)>abs(j)-1):
            print(abs(i),end='')
        else:
            print(' ',end='')
    print()

