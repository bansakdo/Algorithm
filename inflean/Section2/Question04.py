import sys

sys.stdin = open("input.txt", "rt")

# 4번 문제. 대표값

# 내가 푼거
'''
N = int(input())
arr = list(map(int, input().split()))

average = float(sum(arr)) / N
average = round(average)

gap = sys.maxsize
closest_score = 0
index = 0

for i in range(0, N):
    if gap > abs(average - arr[i]):
        index = i + 1
        closest_score = arr[i]
        gap = abs(average - arr[i])
    elif gap == abs(average - arr[i]):
        if closest_score < arr[i]:
            closest_score = arr[i]
            index = i + 1
print(average, index)
'''

# 해설
n = int(input())
a = list(map(int, input().split()))
# ave = round(sum(a)/n)
ave = int(sum(a)/n + 0.5)
minimum = 2147000000
for idx, x in enumerate(a):         # index 번호와 값을 한번에 대입
    tmp = abs(x-ave)
    if tmp < minimum:
        minimum = tmp
        score = x
        res = idx+1
    elif tmp == minimum:
        if x > score:
            score = x
            res = idx+1
print(ave, res)

'''
round는 round_half_even 방식이다.
round_half_even은 반올림 할 때을 소수 부분이 정확히 .5일 경우, 짝수쪽으로 반올림한다.
예를 들면 
4.5일 경우 내림을 하면 4(짝수), 올림을 하면 5(홀수)이므로 결과는 4
5.5일 경우 내림을 하면 5(홀수), 올림을 하면 6(짝수)이므로 결과는 6
따라서 결과가 달라질 수 있으므로 아래의 방법을 사용한다.
a = 4.5
a += 0.5
a = int(a)
소수점 반올림 할 경우에는
a = floor(a)
'''




