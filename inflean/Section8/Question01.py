import sys

sys.stdin = open("input.txt", "rt")


# 1번 문제. 네트워크 선 자르기(Bottom Up)

# 내 풀이
'''

n = int(input())

cnt = 0
max_2m = n // 2
num1 = n
num2 = 0
while num2 <= max_2m:
    if num2 == 0:
        cnt += 1
    else:
        tot = num1 + num2
        for i in range(tot):


    num1 -= 2
    num2 += 1
'''


# 해설
'''
다이나믹 프로그래밍
f(1), f(2)등을 통해 점화식 f(n)을 구하고 이를 통해 푸는 방법

맨 마지막 한칸 빼고 나머지의 경우의 수는 앞에서 이미 구함(f(n-1))
자르는 단위는 1, 2밖에 없으므로, 마지막 2칸이 차지되었을 때는 f(n-2)의 경우의 수.
따라서 f(n)은 f(n-2) + f(n-1) (n은 선의 길이)

f(1) = 1
f(2) = 2
f(3) = 3
f(4) = 5
...
f(n) = f(n-2) + f(n-1)
'''

n = int(input())
dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2
for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])
