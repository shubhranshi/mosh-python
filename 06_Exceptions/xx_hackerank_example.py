test_cases = int(input())
for i in range(test_cases):
    a, b = input().split(" ")
    try:
        print(int(a)//int(b))
    except (ZeroDivisionError, ValueError) as err:
        print('Error Code:', err)


# input
# 3
# 1 0
# 2 $
# 3 1