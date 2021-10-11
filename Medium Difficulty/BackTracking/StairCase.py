

def stairCase(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return stairCase(n-1) + stairCase(n-2)


print(stairCase(3))