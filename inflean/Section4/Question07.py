import sys

sys.stdin = open("input.txt", "rt")

# 7번 창고정리

# 내 풀이
'''
l = int(input())                            # 가로 길이
boxes = list(map(int, input().split()))     # 각 세로 길이
m = int(input())                            # 조정 횟수

for _ in range(m):
    # print(boxes)
    highest = max(enumerate(boxes), key=lambda x: x[1])         # 현재 가장 높은 박스의 위치와 높이 저장
    lowest = min(enumerate(boxes), key=lambda x: x[1])          # 현재 가장 낮은 박스의 위치와 높이 저장
    boxes[highest[0]] -= 1                  # 가장 높은 박스의 높이 -1
    boxes[lowest[0]] += 1                   # 가장 낮은 박스의 높이 +1
# print(boxes)
highest = max(boxes)                        # 가장 높은 박스의 높이
lowest = min(boxes)                         # 가장 낮은 박스의 높이
print(highest - lowest)
'''


# 해설
# 입력받은 것들을 매번 조정하면서 sort 하고, 가장 큰 값과 작은 값의 차를 출력
L = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
for _ in range(m):
    a[0] += 1               # 가장 작은 값 + 1
    a[L-1] -= 1             # 가장 큰 값 - 1
    a.sort()                # 재정렬
print(a[L-1] - a[0])
