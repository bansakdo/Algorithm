
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
    for i in range(1, len(pressedLine[line]) + 1):
        if pressedLine[line][-i] <= fret:
            cnt = i - 1
            break

    move += cnt
    if cnt != 0:
        pressedLine[line] = pressedLine[line][:-cnt]
    if pressedLine[line][-1] != fret:
        pressedLine[line].append(fret)
        move += 1

print(move)




