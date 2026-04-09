from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    
    def compare(a, b):
        if a + b > b + a:
            return -1
        elif b + a > a + b:
            return 1
        return 0
    numbers.sort(key=cmp_to_key(compare))
    
    if numbers[0] == "0":
        return "0"
    
    return "".join(numbers)