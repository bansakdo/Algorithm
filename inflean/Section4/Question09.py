import sys

sys.stdin = open("input.txt", "rt")

# 9번 문제

# 내 풀이
# '''
n = int(input())
arr = list(map(int, input().split()))
res = []
direction = ""
while True:
    # 삼항연산자 : (True 값) if (조건) else (False 값)
    # res가 비었거나 arr의 양 끝이 둘 다 res 마지막값보다 클 때
    if (len(res) == 0 or res[-1] < (arr[0] if arr[0] < arr[-1] else arr[-1])) and len(arr) >= 2:
        flag = 2
    # arr 양 끝 값 둘 다 res 마지막보다 클 때.
    elif res[-1] > (arr[0] if arr[0] > arr[-1] else arr[-1]):
        break
    else:
        flag = 1
    if flag == 2 :
        if arr[0] > arr[-1]:
            res.append(arr[-1])
            arr.pop(-1)
            direction += 'R'
        else:
            res.append(arr[0])
            arr.pop(0)
            direction += 'L'
    elif flag == 1:
        if arr[0] < arr[-1]:
            res.append(arr[-1])
            arr.pop(-1)
            direction += 'R'
        else:
            res.append(arr[0])
            arr.pop(0)
            direction += 'L'

print(len(res))
print(direction)
# '''

# 풀이
'''
lt와 rt를 정함

'''
'''
n = int(input())
a = list(map(int, input().split()))
lt = 0
rt = n - 1
last = 0
res = ""
tmp = []
while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)
'''