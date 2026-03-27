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

list=[1,2,3,4,5,6,7]
m = 2
result = []
perm(list, m, [False]*7, [], result)

print(result)


# # [중복 순열]
# def perm_dup(arr, m, curr, result): 
#     if len(curr) == m:
#         result.append(curr[:])
#         return
#     for i in range(len(arr)):  # used 체크 없음 (중복허용)
#         curr.append(arr[i])
#         perm_dup(arr, m, curr, result)
#         curr.pop()
