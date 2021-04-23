import sys

sys.stdin = open("input.txt", "rt")


# 10번 문제. 스도쿠 검사

# 내가 푼거
'''
def isOrdered(_list):               # 1~9 모두 있는지 확인하는 함수
    for k in range(1, 10):          # 1~9 의 갯수가 모두 1인지 확인
        if _list.count(k) != 1:
            return False
    else:
        return True


matrix = [[int(x) for x in input().split()] for _ in range(9)]
sub_matrix = []

for i in range(3):                                  # 그룹을 sub_matrix에 2차리스트로 저장.
    for j in range(3):
        tmp = matrix[i * 3][3 * j:3 * j + 3]
        tmp += matrix[i * 3 + 1][3 * j:3 * j + 3]
        tmp += matrix[i * 3 + 2][3 * j:3 * j + 3]
        sub_matrix.append(tmp)

for i in range(9):
    col = [matrix[x][i] for x in range(9)]
    if not (isOrdered(matrix[i]) and isOrdered(col) and isOrdered(sub_matrix[i])):
        print("NO")
        break
else:
    print("YES")
'''


# 해설

def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
