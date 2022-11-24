while True:
    n=int(input())
    if n>=2 and n<=10:
        break
    else:
        #print('Enter Valid Number 2 -10 !')
        continue
arry=[]
for i in range(n):
    x=int(input())
    arry.append(x)

arry=list(arry)
x = max(arry)
y = -9999999
for i in range(0, n):
    if arry[i] < x and arry[i] > y:
        y = arry[i]

print(y)


