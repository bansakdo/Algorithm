
# 내 풀이

# def solution(enter, leave):
#     N = len(enter)
#     meet = [set() for _ in range(N+1)]
#     byPerson = [[0, 0] for _ in range(N+1)]
#
#     for i in range(N):
#         byPerson[enter[i]][0] = i
#         byPerson[leave[i]][1] = i
#
#     for i in range(1, N+1):
#         e1, l1 = byPerson[i]
#         earlier_leave = leave[:l1]
#         for el in earlier_leave:
#             e2 = byPerson[el][0]
#             l2 = byPerson[el][1]
#             if e2 > e1:
#                 meet[i].add(el)
#                 meet[el].add(i)
#             else:
#                 for eel in earlier_leave[:l2]:
#                     e3 = byPerson[eel][0]
#                     if e3 > e2 and e3 > e1:
#                         meet[i].add(el)
#                         meet[el].add(i)
#
#     return [len(m) for m in meet[1:]]



# 다른사람 풀이

def solution(enter, leave):
    answer = [0] * len(enter)

    room = []
    e_idx = 0
    for l in leave:
        while l not in room:
            room.append(enter[e_idx])
            e_idx += 1
        room.remove(l)
        for p in room:
            answer[p - 1] += 1
        answer[l - 1] += len(room)

    return answer



# enter = [1, 3, 2]
# leave = [1, 2, 3]
# [0, 1, 1]

enter = [1, 4, 2, 3]
leave = [2, 1, 3, 4]
# [2, 2, 1, 3]
print(solution(enter, leave))

