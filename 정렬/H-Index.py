def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    for i in range(len(citations)):
        count = i+1
        if count > citations[i]:
            return count-1
            
    return len(citations)