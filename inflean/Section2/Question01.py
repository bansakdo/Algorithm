import sys

sys.stdin = open("input.txt", "rt")  # 파일 읽어오는 방법 rt는 모드

# 1번 문제. K번째 약수

# 내가 만든거
'''
n, k = input().split()
n = int(n)
k = int(k)
num = int(0)
for i in range(1, n+1):
    if n % i == 0:
        num += 1
        if num == k:
            print(i)
            break
else:
    print(-1)
'''

# 해설
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt+=1
    if cnt == k:
        print(i)
        break
else:
    print(-1)

