while True:
    a = int(input())
    b = int(input())
    if a>=1 and a<=pow(10, 10) and b>=1 and b<=pow(10, 10):
        break
    else:
        print('Please enter valid number 1-pow(10, 10)!')
        continue
print(a+b)
print(a-b)
print(a*b)