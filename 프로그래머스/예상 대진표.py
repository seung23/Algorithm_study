
def solution(n,a,b):
    answer = 0
    if a%2 == 1:
        a += 1
    if b%2 == 1:
        b += 1
    # 12 34 56 78 -> # 1 2 3 4 -> # 1 2
    count = 1
    while abs(b-a) > 1:
        a = a//2
        b = b//2
        if a%2 == 1:
            a += 1
        if b%2 == 1:
            b += 1
        count += 1

    return count