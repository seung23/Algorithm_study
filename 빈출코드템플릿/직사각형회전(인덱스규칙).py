### 직사각형 ###
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # n, m = 3, 4

def rotated_90(arr): 
    n = len(arr) 
    m = len(arr[0]) 
    result = [[0]*n for _ in range(m)] # 행 <-> 열 뒤집힘 주의(4x3)
    for i in range(n): 
        for j in range(m): 
            result[j][n-1-i] = arr[i][j]
    return result

def rotated_180(arr): 
    n = len(arr) 
    m = len(arr[0]) 
    result = [[0]*m for _ in range(n)] # 원래대로(3x4)
    for i in range(n): 
        for j in range(m): 
            result[n-1-i][m-1-j] = arr[i][j]
    return result

def rotated_270(arr):
    n = len(arr)
    m = len(arr[0])
    result = [[0]*n for _ in range(m)] # 행 <-> 열 뒤집힘 주의(4x3)
    for i in range(n):
        for j in range(m):
            result[m-1-j][i] = arr[i][j]
    return result


for a in arr:
    print(*a)
print("___________\n")

a90 = rotated_90(arr)
for a in a90:
    print(*a)
print("___________\n")  
a180 = rotated_180(arr)
for a in a180:
    print(*a)
print("___________\n")    
a270 = rotated_270(arr)
for a in a270:
    print(*a)