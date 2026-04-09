from collections import deque

def solution(priorities, location):
    
    idx_prior = deque(enumerate(priorities))
    answer = 0 
    priorities.sort(reverse=True)
    priorities = deque(priorities)
    while idx_prior:
        a = idx_prior.popleft()
        if a[1] != priorities[0]:
            idx_prior.append(a)
        else:
            priorities.popleft()
            answer += 1
            if a[0] == location:
                return answer
    
    return answer