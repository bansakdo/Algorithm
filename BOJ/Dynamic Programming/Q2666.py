


def func(needs, open, n, idx):
    if idx == len(needs):
        return 0
    rst = n * len(needs)
    open.sort()
    this_time = needs[idx]
    avail = []
    if this_time in open:
        idx += 1
        if idx == len(needs):
            return 0
        this_time = needs[idx]
    for i in range(len(open)):
        if this_time < open[i]:
            avail.append(open[i])
            break
        elif i == len(open) - 1:
            avail.append(open[i])
        elif open[i] < this_time < open[i + 1]:
            avail.append(open[i])
            avail.append(open[i + 1])
            break

    for a in avail:
        i = open.index(a)
        open.pop(i)
        num = abs(a - this_time)
        open.insert(i, this_time)
        num += func(needs, open, n, idx + 1)
        rst = min(rst, num)
        open.pop(i)
        open.insert(i, a)

    return rst

N = int(input())
opens = sorted(list(map(int, input().split())))
move_num = int(input())
needs = list(int(input()) for _ in range(move_num))

print(func(needs, opens, N, 0))


