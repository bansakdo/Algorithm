import sys

sys.stdin = open("input.txt", "rt")

# 5번 문제. 회의실 배정(그리디)

'''
n = int(input())

meetings = [[int(x) for x in input().split()] for _ in range(n)]

meetings.sort()
# print(meetings)
times = [int(y-x) for x, y in meetings]

max_time = max(times)
res = []
cnt = 0

sorted_list = sorted(enumerate(times), key=lambda x: x[1])               # 1번 인덱스를 기준으로 오름차순 정렬

# print("e:", e_list)
# print(len(sorted_list))


for x in sorted_list:
    s = meetings[x[0]][0]
    e = meetings[x[0]][1]

    if len(res) == 0:
        res.append(meetings[x[0]])
        cnt += 1
        continue
    for y in res:
        # if s == y[0] and e == y[1]:
        #     res.append(meetings[x[0]])
        #     cnt += 1
        #     break
        if y[0] < s < y[1] or y[0] < e < y[1] or (s < y[0] and e > y[1]) or (s == y[0] and e > y[1]) or (s < y[0] and e == y[1]):
            break
    else:
        res.append(meetings[x[0]])
        cnt += 1
#
# for i in range(1, max_time + 1):
#     m_list = []                             # 현재 배정된 회의
#     for j in range(n):
#         if times[j] == i:
#             m_list.append(meetings[j])
#     print(i, m_list)
#
#     for x in m_list:
#         s = x[0]
#         e = x[1]
#
#         for y in res:
#             # if s < e <= y[0] or y[1] <= s < e:
#             #     continue
#             # else:
#             #     break
#             if s == y[0] and e == y[1]:
#                 continue
#             if y[0] < s < y[1] or y[0] < e < y[1] or (s <= y[0] and e >= y[1]):
#                 break
#         else:
#             res.append(x)
#             cnt += 1

print()
print(cnt)

res.sort()
# print(res)

'''

# 그리디는 보통 정렬과 동반
# 끝나는 시간으로 정렬
# 끝나는 시간과 다음 시작하는 시간을 비교

'''
n = int(input())

meetings = [[int(x) for x in input().split()] for _ in range(n)]

sorted_list = sorted(meetings, key=lambda x: x[1])               # 1번 인덱스를 기준으로 오름차순 정렬
cnt = 0
last = 0

for x in sorted_list:
    if x[0] >= last:
        cnt += 1
        last = x[1]
print(cnt)
'''

# 해설
# '''
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

# 끝나는 시간 기준으로 정렬
print(meeting)
meeting.sort(key=lambda x: (x[1], x[0]))
print(meeting)
et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1
print(cnt)
# '''

