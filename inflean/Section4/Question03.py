import sys
import time

sys.stdin = open("input.txt", "rt")

start = time.time()

# 3번 문제. 뮤직비디오(결정 알고리즘)

'''
# def confirmIsLast(divider, last_idx):
#     if divider[len(divider) - 1 - last_idx] == (m - 1 - last_idx):
def confirmIsLast(divider, last_idx):
    idx = len(divider) - 1 - last_idx
    # print("f_idx:", idx)
    # print(divider[idx])
    # print(n - 1 - last_idx)
    if divider[idx] == (n - 1 - last_idx):
        if idx == 0:
            return True
        elif divider[idx] - divider[idx - 1] == 1:
            return confirmIsLast(divider, last_idx + 1)
        else:
            divider[idx - 1] += 1
            divider[idx] = divider[idx - 1] + 1
    else:
        divider[idx] += 1
        return False


n, m = map(int, input().split())            # n: 곡, m: DVD
songs = list(map(int, input().split()))

divider = [int(x) for x in range(1, m)]
min_size = sum(songs)
size = [int(0) for _ in range(m)]

while True:
    dvd = []
    tmp_largest_size = 0
    for i in range(m):
        if i == 0:
            dvd.append(songs[:divider[i]])
        elif i == m-1:
            dvd.append(songs[divider[i - 1]:])
        else:
            dvd.append(songs[divider[i - 1]: divider[i]])
        # size[i] = sum(dvd[i])
        if i != 0 and size[i] > tmp_largest_size:
            tmp_largest_size = size[i]
    print("dvd:",dvd)
    # temp_size = list(map(sum, dvd))
    # largest_size = max(temp_size)
    # if largest_size < min_size:
    #     min_size = largest_size
    # tmp_largest_size = max(list(map(sum, dvd)))
    if tmp_largest_size < min_size:
        min_size = tmp_largest_size

    if confirmIsLast(divider, 0):
        break

print(min_size)
'''


'''
n, m = map(int, input().split())            # n: 곡, m: DVD
songs = list(map(int, input().split()))
lt = 1
rt = sum(songs)
res = 0
while lt <= rt:
    sum_songs = 0
    mid = (rt + lt) // 2
    cnt = 1
    for x in songs:
        if cnt > m:
            break
        # sum_songs += x
        if (sum_songs + x) > mid:
            sum_songs = x
            cnt += 1
        else:
            sum_songs += x

    print()
    print(lt, rt)
    print(mid)
    print(cnt)
    if cnt <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)
'''


# 해설
# '''
def Count(capacity):
    cnt = 1
    sum = 0
    for x in Music:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

n, m = map(int, input().split())
Music = list(map(int, input().split()))
lt = 1
rt = sum(Music)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    cc = Count(mid)
    print()
    print(lt, rt)
    print(mid)
    print(cc)
    if cc <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)
# '''



print("time :", time.time() - start)
