arr = [[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]]

for ar in arr:
    print(*ar)

print("_____________\n")
# 시계 방향 90 (= 반시계 방향 270)
arr_90 = list(map(list, zip(*arr[::-1])))
# arr 행 순서 뒤집고 zip(*)로 전치
for ar_90 in arr_90:
    print(*ar_90)


print("_____________\n")

# 시계 방향 180 (= 반시계 방향 180)
arr_180 = [a[::-1] for a in arr[::-1]]
# arr의 행 순서 뒤집은 각 행을 a로 받아서 하나씩 행 원소 순서 뒤집기
for ar_180 in arr_180:
    print(*ar_180)


print("_____________\n")

# 시계 방향 270 (= 반시계 방향 90)
arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]
# 90도 회전 후 행 순서 뒤집고 각 행을 x로 받아서 하나씩 행 원소 순서 뒤집기
for ar_270 in arr_270:
    print(*ar_270)

