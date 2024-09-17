# 運用清單存取算出此清單中奇數位資料相乘除以偶數位資料。

b = [2,1,4,8,9,3] 

# step1 找出所有 奇數位資料 

list1=[ b[0] , b[2] , b[4] ]
print(list1) 

# step2 找出所有 偶數位資料 

list2=[ b[1] , b[3] , b[5] ]
print(list2) 

#step3 奇數位資料相乘存a1 偶數位資料相乘存a2
a1 = a2 = 1
for i in range(0, len(b), 2):
    print(i,b[i])
    a1 = a1*b[i]
for i in range(1, len(b), 2):
    print(i,b[i])
    a2 = a2*b[i]

#step4 a1/a2 印出結果
print(a1/a2)

#range(開始（含本身），結束（不含本身），間隔值)
#len（變數）知道長度，變數可以是list，可以是字串

for i in range(len(b)):
    print(b[i]*2,end = " ")
print()