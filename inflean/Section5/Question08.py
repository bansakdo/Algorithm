import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

# 8번 문제. 단어 찾기

# 내 풀이
'''
n = int(input())
word = deque(input() for _ in range(n))

for _ in range(n-1):
    writed = input()
    for i in range(n):
        if word[0] == writed:
            word.popleft()
            break
        else:
            word.append(word.popleft())
print(word[0])
'''

# 해설
n = int(input())
p = dict()                      # 닥셔너리. String을 key로 사용 가능.
for i in range(n):
    word = input()
    p[word] = 1                 # key가 word 인 것에 value를 1로 함.
for i in range(n-1):
    word = input()
    p[word] = 0                 # key가 word 인 것에 value를 0로 함. 따라서 빠진 단어는 1번 인덱스가 1이다.

for key, val in p.items():      # p의 key, value 동시에 접근
    if val == 1:                # val의 값이 1이면 key 출력
        print(key)
        break



