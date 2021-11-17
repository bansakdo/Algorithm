import sys

sys.stdin = open("input.txt", "rt")


# 2번 문제. 쇠막대기

# 내 풀이
'''
stick = input()

stack = []
a = 0                       # 현대 겹쳐진 쇠막대기 수
cnt = 0                     # 현재 잘려진 쇠막대기 수
last = ''
for x in stick:
    if x == '(':            # 쇠막대기 시작
        a += 1              # 한개 더 겹치거나 레이저 준비
        stack.append(a)
    elif x == ')':          # 레이저로 자르거나 쇠막대기 끝남.
        a -= 1
        stack.pop()
        if last == '(':     # 직전이 ( 이면 레이저
            cnt += a        # 겹친 개수만큼 추가
        else:               # 아니면 막대기 길이가 끝남
            cnt += 1        # 1만 추가.
    last = x
print(cnt)
'''

# 해설
s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)


