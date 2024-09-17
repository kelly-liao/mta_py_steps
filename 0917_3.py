# 練習3
# A
# B
# C
# D
# E

# ABCDE
# way 1
for i in range(5):
    print('*')
print()
for i in range(5):
    print('*',end='')
print()
print()

for i in range(5):
    print(i+1)
print()
for i in range(5):
    print((i+1),end='')
print()
print()

for i in range(5):
    print(chr(i+65))
print()
for i in range(5):
    print(chr(i+65),end='')
print()
print()

# way 2
list1 = ['A','B','C','D','E']
for i in range (5):
    print(list1[i])
print()
for i in range(5):
    print(list1[i],end='')
print()