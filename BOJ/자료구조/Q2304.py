from collections import Counter


N = int(input())
pillar = [list(map(int, input().split())) for _ in range(N)]
pillar.sort(key=lambda x: x[0])

max_height = max(pillar, key=lambda x: x[1])[1]
height_count = Counter(list(zip(*pillar))[1])
max_height_num = height_count[max_height]
area = 0
x, y = pillar[0][0], 0

for i in range(len(pillar)):
    p = pillar[i]
    if max_height_num > 0:
        if p[1] >= y:
            area += (p[0] - x) * y
            x = p[0]
            y = p[1]
        if p[1] == max_height:
            area += y
            x += 1
            max_height_num -= 1
    else:
        max_height = max(pillar[i:], key=lambda x: x[1])[1]
        if max_height == p[1]:
            y = p[1]
            area += (p[0] - x + 1) * y
            x = p[0] + 1

print(area)





