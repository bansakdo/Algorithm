import sys

sys.stdin = open("input.txt", "rt")


# 2번 문제. 숫자만 추출

# 내가 푼거
'''
in_s = input()
length = len(in_s)
num_s = ''

for x in in_s:
    x = ord(x)
    if x >= 48 and x <= 57:
        num_s += chr(x)
num = int(num_s)
print(num)

cnt = 2
for i in range(2, num):
    if num % i == 0:
        cnt += 1

print(cnt)
'''

# 해설
s = input()
res = 0
for x in s:
    # isdecimal(): 0~9 찾아줌.
    # isdigit(): 숫자인지만 판별. 큰 숫자도 가능.
    if x.isdecimal():
        res=res*10+int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)