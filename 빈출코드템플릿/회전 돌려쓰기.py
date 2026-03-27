### 정사각형 ###
n = 3  # (3x3 정사각형)
arr = [[1,2,3],[4,5,6],[7,8,9]]

for a in arr:
    print(*a)
print("___________\n")

def rotate_90(arr):
    arr_90 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_90[j][n-1-i] = arr[i][j]
    return arr_90

def rotate_90_manytime(arr, times):
    for _ in range(times):
        arr = rotate_90(arr)
    return arr

arr1 = rotate_90_manytime(arr, 3)

for a in arr1:
    print(*a)




