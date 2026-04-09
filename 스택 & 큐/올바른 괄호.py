from collections import deque

def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append('1')
        elif s[i] == ")":
            if not stack:
                return False
            stack.pop()
                
    if not stack:
        return True
    
    return False
    