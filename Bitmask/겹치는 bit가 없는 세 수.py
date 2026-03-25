n = int(input())
arr = list(map(int, input().split()))

max_val = 0 

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a, b, c = arr[i], arr[j], arr[k]
            if a & b == 0 and a & c == 0 and b & c == 0:
                max_val = max(max_val, a+b+c)

print(max_val)