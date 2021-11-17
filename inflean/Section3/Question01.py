import sys

sys.stdin = open("input.txt", "rt")

# 1번 문제. 회문 문자열 검사

# 내가 푼거
'''
n = int(input())
for i in range(n):
    input_str = str(input())
    input_str = input_str.lower()

    length = len(input_str)
    # 문자열의 길이의 반 까지만 반복문을 돌릴 수 있도록 길이 조정
    if length % 2 == 1:
        l = int(length / 2) + 1
    elif length % 2 == 0:
        l = int(length / 2)
    # l = int(length / 2) + (length % 2)

    rst = "YES"
    for j in range(l):
        if j != length - 1:
            if input_str[j] != input_str[length - 1 - j]:
                rst = "NO"
                break
        else:                   # 문자열의 길이가 홀수일 때 j가 문자열의 중간인 인덱스와 같은 값일 경우
            break

    print("#%d" % (i+1), rst)
'''

# 해설
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size // 2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

    # 파이썬 내장함수 사용.
    # 파이썬 내장함수 말고 직접 하는것이 중요.
    # if s == s[::-1]:
    #     print("#%d YES" %(i+1))
    # else:
    #     print("#%d NO" %(i+1))