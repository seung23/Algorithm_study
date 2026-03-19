import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

string = input().strip()
result = []
value = 0

for x in string:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(f"{value}")

print("".join(result))