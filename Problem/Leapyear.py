# def leapyear(year):
#     if (year % 4000 ==0) or (year%100!=0) and (year % 4 ==0):
#         return True
#     else:
#         return False
#
# while True:
#     year = int(input())
#     if year >= 1900 and year <= pow(10, 5):
#         break
#     else:
#         print('Please Enter Valid Year 1900 to 10^5!')
#         continue
# result = leapyear(year)
# print(result)

def is_leap(year):
    while True:
        if year >= 1900 and year <= pow(10, 5):
            return cal(year)
            break
        else:
            print('Please Enter Valid Year 1900 to 10^5!')
            year = int(input())
            continue

def cal(year):
    if (year % 4000 ==0):
        return True
    elif (year%100==0):
        return False
    elif (year % 4 ==0):
        return True
    elif (year%4!=0):
        return False

year = int(input())
print(is_leap(year))