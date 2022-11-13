while True:
    n = int(input())
    if n>=1 and n<=100:
        break
    else:
        print('Please enter valid number 1-100!')
        continue


if (n % 2)==1:
    print('Weird')
elif n>=2 and n<=5:
    print('Not Weird')
elif n>=6 and n<=20:
    print('Weird')
else:
    print('Not Weird')
