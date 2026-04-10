def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s, i):
            answer += 1
    
    return answer

def check(s, j):
    stack = []
    for i in range(j, len(s)+j):
        k = i%len(s)
        if s[k] in "[{(":
            stack.append(s[k])
        elif s[k] == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif s[k] == ")":
            if stack and stack[-1] == "(":                
                stack.pop()
            else:
                return False
        elif s[k] == "}":
            if stack and stack[-1] == "{" :
                stack.pop()
            else:
                return False
            
    if not stack:
        return True