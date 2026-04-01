import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]

def find_bottom(si, sj, ei, ej):
    for i in range(ei, n+1):
        if sum(arr[i][sj:ej]) != 0:
            return i
    return n+1

def mark(num, si, sj, ei, ej):
    for i in range(si, ei):
        arr[i][sj:ej] = [num]*(ej-sj)

def drop(num):
    si, sj, ei, ej = unit[num]
    bottom_i = find_bottom(si, sj, ei, ej)
    n_si, n_ei = bottom_i - (ei-si), bottom_i
    mark(0, si,sj,ei,ej)
    mark(num, n_si, sj, n_ei, ej)
    unit[num] = [n_si, sj, n_ei, ej]



def gravity(si, sj, ei, ej): # 위로 올라가면서 부딪히는 박스 찾기
    sset = set()
    for i in range(si-1, 0, -1):
        for j in range(sj, ej):
            if arr[i][j] != 0 and arr[i][j] not in sset:
                drop(arr[i][j])
                sset.add(arr[i][j])



unit = {}
v = [0]*101
for _ in range(m):
    k, h, w, c = map(int, input().split())
    si, sj, ei, ej = 1, c, 1+h, c+w
    bottom_i = find_bottom(si, sj, ei, ej)
    n_si, n_ei = bottom_i - h, bottom_i
    mark(k, n_si, sj, n_ei, ej)
    unit[k] = [n_si, sj, n_ei, ej]
    v[k] = 1

# 오름차순으로 박스 내릴 수 있는지 체크 후 내리기 -> 총 m번하면 박스는 없을 것.
# 왼쪽 -> 중력 -> 오른쪽 -> 중력 반복되도록 어떻게 짤까?
# 똑같은 구조로 짜되 flag로 바뀌도록 하자.
left = True
ans = []
for _ in range(m):
    for num in range(1, 101):
        if v[num] == 0:
            continue

        si,sj,ei,ej = unit[num]
        for i in range(si, ei):
            if left == True:
                if sum(arr[i][1:sj]) != 0:
                    break
            else:
                if sum(arr[i][ej:n+1]) != 0:
                    break

        else:
            mark(0, si, sj, ei, ej)
            v[num]=0
            ans.append(num)
            gravity(si, sj, ei, ej)
            break

    left = not left

for a in ans:
    print(a)