import sys

sys.stdin = open("input.txt", "rt")


# 4번 문제. 마구간 정하기

'''
def measure(horse, l, r):
    distance = 0
    mid = (l + r) // 2
    left = stable[mid] - stable[l]
    right = stable[r] - stable[mid]
    print()
    print(stable[l:r+1])
    print(horse)
    print(l)
    print(r)
    print(mid)
    print(left)
    print(right)
    # if left < right:
    #     horse -= (r - mid) // 2
    #     r = mid
    #     distance = left
    # elif left > right:
    #     horse -= (mid - l) // 2
    #     l = mid
    #     distance = right
    # elif left == right and horse > 2:
    if horse > 2:
        # lm = measure(horse - (mid - l) // 2, mid, r)
        # rm = measure(horse - (r - mid) // 2, l, mid)
        lm = measure(horse // 2, mid, r)
        rm = measure(horse // 2, l, mid)
        if lm < rm:
            distance = lm
        else:
            distance = rm
        # break
    else:
        # print("same!!!!")

        distance = stable[r] - stable[l]
        # print("else distance:", distance)
    print()
    print(distance)
    return distance


n, c = map(int, input().split())

stable = [int(input()) for _ in range(n)]

stable.sort()
horse = c
lt = 0
rt = n - 1

print(stable)
distance = 0

distance = measure(horse, lt, rt)

print("\n---------")
print(distance)
'''



'''
n, c = map(int, input().split())

stable = [int(input()) for _ in range(n)]

stable.sort()
horse = c
lt = 0
rt = n - 1
print(lt, rt)
res = 0
print(stable[0:4])


while lt < rt:
    mid = (lt + rt) // 2
    mid_val = (stable[lt] + stable[rt]) // 2

    print()
    print(lt)
    print(rt)
    print(mid)

    tmp_d = 0
    cnt = 0
    for x in stable:
        if tmp_d + x > mid_val:
            cnt+=1
            tmp_d = x
        else:
            tmp_d += x
    print(cnt)

    if cnt < c:
        rt = mid
    else:
        lt = mid
        res = mid

print("\n----------")
print(res)
'''


# 해설

def Count(len):
    cnt = 1
    ep = Line[0]
    for i in range(1, n):
        if Line[i] - ep >= len:
            cnt += 1
            ep = Line[i]
    return cnt


n, c = map(int, input().split())
Line = []
for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort()

lt = 1
rt = Line[n-1]

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)




