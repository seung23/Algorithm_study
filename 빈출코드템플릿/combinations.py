def comb(arr, m, start, curr, result):
    if len(curr)==m:
        result.append(curr[:])
        return
    for i in range(start, len(arr)):
        curr.append(arr[i])
        comb(arr, m, i+1, curr, result)
        curr.pop()

list=[1,2,3,4,5,6,7]
m = 2
result = []

comb(list, m, 0, [], result)
print(result)


# # [중복 조합]
# def comb_dup(arr, start, m, curr, result):
#     if len(curr) == m:
#         result.append(curr[:])
#         return
#     for i in range(start, len(arr)):
#         curr.append(arr[i])
#         comb_dup(arr, i, m, curr, result)  # i: 자기자신부터 (중복허용)
#         curr.pop()
