import sys
'''
INPUT
7
2
1
4
5
1
3
3


'''

# 1725번. 히스토그램
'''
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
res = 0
# bottom = [0] * 2


for i in range(n):
    for j in range(i, n):
        if (j - i + 1) < res and 1 in arr[i:j+1]:
            break
        if i == j and arr[i] < res:
            continue
        square = (j - i + 1) * min(arr[i:j+1])
        res = max(res, square)
print(res)
'''

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.append(0)                   # 나중에 범위 오류 방지
cursor = 0
res = 0
stack = [(0, arr[0])]
for i in range(1, n+1):
    cursor = i
    while stack and stack[-1][1] > arr[i]:
        cursor, tmp = stack.pop()
        res = max(res, tmp * (i - cursor))
    stack.append((cursor, arr[i]))
print(res)


