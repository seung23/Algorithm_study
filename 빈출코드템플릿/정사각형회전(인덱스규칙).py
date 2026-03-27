### 정사각형 ###
n = 3  # (3x3 정사각형)
arr = [[1,2,3],[4,5,6],[7,8,9]]

for a in arr:
    print(*a)
print("___________\n")

arr_90 = [[0]*n for _ in range(n)]
for i in range(n): 
    for j in range(n): 
        arr_90[j][n-1-i] = arr[i][j] # (n-1) = max_r (0-indexed에서 마지막 인덱스 2)

for a in arr_90:
    print(*a)
print("___________\n")

arr_180 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_180[n-1-i][n-1-j] = arr[i][j]

for a in arr_180:
    print(*a)
print("___________\n")

arr_270 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_270[n-1-j][i] = arr[i][j]

for a in arr_270:
    print(*a)
print("___________\n")



