arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]  # (7n7) 행렬

start_n, start_m = 2, 3  # 행, 열
length = 3

for a in arr:
    print(*a)
print("___________\n")

#정사각형 배열의 특정 부분만 회전시키는 함수
def partial_rotate_90(arr, start_n, start_m, length):
    new_arr = [row[:] for row in arr]  # 깊은 복사, [:]가 있으면 새로운 리스트를 반환
                                       # [:]가 없으면 얕은 복사여서 그대로 참조(원본값 변환 위험)

    for n in range(start_n, start_n + length):
        for m in range(start_m, start_m + length):
            on, om = n - start_n, m - start_m
            rn, rm = om, length - 1 - on
            new_arr[start_n + rn][start_m + rm] = arr[n][m]

    return new_arr

def partial_rotate(arr, start_n, start_m, length, times):   # 사실 180도 270도 따로 외울필요없이 90도를 반복 호출하는게 더 나은듯
    for _ in range(times):
        arr = partial_rotate_90(arr, start_n, start_m, length)
    return arr

arr1 = partial_rotate(arr, start_n, start_m, length, times=1)  # 90도
for a in arr1:
    print(*a)
print("___________\n")
arr2 = partial_rotate(arr, start_n, start_m, length, times=2)  # 180도
for a in arr2:
    print(*a)
print("___________\n")
arr3 = partial_rotate(arr, start_n, start_m, length, times=3)  # 270도
for a in arr3:
    print(*a)
print("___________\n")