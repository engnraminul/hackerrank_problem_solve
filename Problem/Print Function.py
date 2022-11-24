while True:
    n = int(input())
    if n <= 150 and n >= 1:
        break
    else:
        print('Please Enter Valid Number (1  to 150 !')
        continue

for a in range(n):
    print(a+1, end="")
