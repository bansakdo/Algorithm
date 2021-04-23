import sys

sys.stdin = open("input.txt", "rt")

# 10번 문제. 점수계산

# 내가 푼거
'''
n = int(input())
answer = [int(x) for x in input().split()]

cnt = 0
score = 0
for i in range(n):
    if answer[i] == 0:
        cnt = 0
    elif answer[i] == 1:
        cnt += 1
        score += cnt

print(score)
'''

# 해설

n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)

