import math

def solution(numbers):
    answer = 0
    perm_result = []
    for i in range(1, len(numbers) + 1):
        used = [False]*len(numbers)
        perm(numbers, i, used, [], perm_result)
    num_cand = []
    for num in perm_result:
        temp = ""
        for i in range(len(num)):
            temp += num[i]
        num_cand.append(temp)
        
    num_set = set(num_cand)
    for num in num_set:
        if num[0] == "0":
            continue
        else:
            count = 0
            for i in range(1, int(math.sqrt(int(num)))+1):
                if int(num)%i == 0:
                    count += 1
        if count == 1 and int(num) >= 2:
            answer += 1
            
    return answer

def perm(arr, m, used, curr, result):
    if len(curr)==m:
        result.append(curr[:])
        return
    for i in range(len(arr)):
        if not used[i]:
            used[i]=True
            curr.append(arr[i])
            perm(arr, m, used, curr, result)
            curr.pop()
            used[i]=False
            
    