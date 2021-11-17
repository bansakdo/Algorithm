import math

N, H = map(int, input().split())
dungeons = [list(map(int, input().split())) for _ in range(N)]
lt = 1
rt = 1
for t, a, h in dungeons:
    if t == 1:
        rt += math.ceil(h / H) * a

rst = 0
while lt <= rt:
    mid = (lt + rt) // 2

    attack = H
    hp = mid
    for t, a, h in dungeons:
        if t == 1:
            numOfFight = min(math.ceil(h / attack), math.ceil(hp / a))
            h -= numOfFight * attack
            hp -= numOfFight * a

            if h <= 0:
                hp += a
                continue
            if hp <= 0:
                break
        else:
            attack += a
            hp += h
            if hp > mid:
                hp = mid

    else:
        rt = mid - 1
        rst = mid

    if hp <= 0:
        lt = mid + 1

print(rst)
