
#
# n, p = map(int, input().split())
#
# # [line, fret]
# melody = [list(map(int, input().split())) for _ in range(n)]
# pressedLine = [[] for _ in range(7)]
#
# move = 0
#
# for line, fret in melody:
#     if not pressedLine[line] or pressedLine[line][-1] < fret:
#         pressedLine[line].append(fret)
#         move += 1
#         continue
#
#     if pressedLine[line][0] > fret:
#         move += len(pressedLine[line])
#         pressedLine[line].clear()
#     else:
#         while pressedLine[line] and pressedLine[line][-1] > fret:
#             pressedLine[line].pop()
#             move += 1
#
#     if not pressedLine[line] or pressedLine[line][-1] != fret:
#         pressedLine[line].append(fret)
#         move += 1
#
# print(move)




#
# n, p = map(int, input().split())
#
# # [line, fret]
# melody = [list(map(int, input().split())) for _ in range(n)]
# pressedLine = [[] for _ in range(7)]
#
# move = 0
#
# for line, fret in melody:
#     # 줄이 비었거나 프렛이 줄 맨 마지막 값보다 큰 경우
#     if not pressedLine[line] or pressedLine[line][-1] < fret:
#         pressedLine[line].append(fret)
#         move += 1
#         continue
#
#     # 프렛이 줄의 맨 앞 값보다 작은 경우
#     if fret < pressedLine[line][0]:
#         move += len(pressedLine[line]) + 1
#         pressedLine[line] = [fret]
#         continue
#
#     # 줄에 이미 들어있는 경우
#     if fret in pressedLine[line]:
#         idx = pressedLine[line].index(fret)
#         move += len(pressedLine[line]) - 1 - idx
#         pressedLine[line] = pressedLine[line][:idx+1]
#         continue
#
#
#     # 들어있지 않고 줄에서 몇개의 손가락을 빼야 하는지 찾아야 하는 경우
#     lt, rt = 0, len(pressedLine[line])
#     rst = 0
#     while lt <= rt:
#         mid = (lt + rt) // 2
#
#         if pressedLine[line][mid] < fret:
#             lt = mid + 1
#             rst = mid
#         else:
#             rt = mid - 1
#
#     move += len(pressedLine[line]) - rst
#     pressedLine[line] = pressedLine[line][:rst + 1]
#     pressedLine[line].append(fret)
#     print(line, pressedLine[line])
#
# print(move)
#



n, p = map(int, input().split())

# [line, fret]
melody = [list(map(int, input().split())) for _ in range(n)]
pressedLine = [[] for _ in range(7)]

move = 0

for line, fret in melody:
    # 줄이 비었거나 프렛이 줄 맨 마지막 값보다 큰 경우
    if not pressedLine[line] or pressedLine[line][-1] < fret:
        pressedLine[line].append(fret)
        move += 1
        continue

    # 프렛이 줄의 맨 앞 값보다 작은 경우
    if fret < pressedLine[line][0]:
        move += len(pressedLine[line]) + 1
        pressedLine[line] = [fret]
        continue

    cnt = 0
    # for i in range(len(pressedLine[line]) - 1, -1, -1):
    #     if pressedLine[line][i] > fret:
    #         cnt += 1
    #     # elif pressedLine[line][i] <= fret:
    #     else:
    #         break
    # print()
    for i in range(1, len(pressedLine[line]) + 1):
        # print(i, fret, pressedLine[line][-i], pressedLine[line])
        if pressedLine[line][-i] <= fret:
            cnt = i - 1
            break

    # print(fret, cnt)
    move += cnt
    # print()
    # print(pressedLine[line], fret, cnt)
    if cnt != 0:
        pressedLine[line] = pressedLine[line][:-cnt]
    # print(pressedLine[line])
    if pressedLine[line][-1] != fret:
        pressedLine[line].append(fret)
        move += 1


print(move)
n, p = map(int, input().split())

# [line, fret]
melody = [list(map(int, input().split())) for _ in range(n)]
pressedLine = [[] for _ in range(7)]

move = 0

for line, fret in melody:
    # 줄이 비었거나 프렛이 줄 맨 마지막 값보다 큰 경우
    if not pressedLine[line] or pressedLine[line][-1] < fret:
        pressedLine[line].append(fret)
        move += 1
        continue

    # 프렛이 줄의 맨 앞 값보다 작은 경우
    if fret < pressedLine[line][0]:
        move += len(pressedLine[line]) + 1
        pressedLine[line] = [fret]
        continue

    cnt = 0
    # for i in range(len(pressedLine[line]) - 1, -1, -1):
    #     if pressedLine[line][i] > fret:
    #         cnt += 1
    #     # elif pressedLine[line][i] <= fret:
    #     else:
    #         break
    # print()
    for i in range(1, len(pressedLine[line]) + 1):
        # print(i, fret, pressedLine[line][-i], pressedLine[line])
        if pressedLine[line][-i] <= fret:
            cnt = i - 1
            break

    # print(fret, cnt)
    move += cnt
    # print()
    # print(pressedLine[line], fret, cnt)
    if cnt != 0:
        pressedLine[line] = pressedLine[line][:-cnt]
    # print(pressedLine[line])
    if pressedLine[line][-1] != fret:
        pressedLine[line].append(fret)
        move += 1


print(move)

'''
1 3 5
2
cnt == 2


'''





