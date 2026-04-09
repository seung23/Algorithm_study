from collections import Counter
from math import prod

def solution(clothes):
    c = Counter([row[1] for row in clothes])
    answer = prod(v + 1 for v in c.values()) - 1
    return answer