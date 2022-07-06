import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
rst = 0

arr = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            arr[i][j] = arr[i-1][j-1] + 1
            rst = max(rst, arr[i][j])

print(rst)
