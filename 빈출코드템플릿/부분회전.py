arr = [[7 * j + i for i in range(1, 8)] for j in range(7)] # (7x7) 행렬

start_x, start_y = 2, 2
length = 3

for a in arr:
    print(*a)
print("___________\n")

#정사각형 배열의 특정 부분만 회전시키는 함수
def partial_rotate_90(arr, start_y, start_x, length):
    n = len(arr)
    new_arr = [row[:] for row in arr]  # 깊은 복사, [:]가 있으면 새로운 리스트를 반환
                                       # [:]가 없으면 얕은 복사여서 그대로 참조(원본값 변환 위험)

    for y in range(start_y, start_y + length):
        for x in range(start_x, start_x + length):
            oy, ox = y - start_y, x - start_x
            ry, rx = ox, length - 1 - oy
            new_arr[start_y + ry][start_x + rx] = arr[y][x]

    return new_arr

def partial_rotate(arr, start_y, start_x, length, times):   # 사실 180도 270도 따로 외울필요없이 90도를 반복 호출하는게 더 나은듯
    for _ in range(times):
        arr = partial_rotate_90(arr, start_y, start_x, length)
    return arr

arr1 = partial_rotate(arr, 2, 2, 3, times=1)  # 90도
for a in arr1:
    print(*a)
print("___________\n")
arr2 = partial_rotate(arr, 2, 2, 3, times=2)  # 180도
for a in arr2:
    print(*a)
print("___________\n")
arr3 = partial_rotate(arr, 2, 2, 3, times=3)  # 270도
for a in arr3:
    print(*a)
print("___________\n")