
N = int(input())
humans = [[*map(int, input().split())] for _ in range(N)]

rst = []
for i in range(N):
    now = humans[i]
    num = 1
    for j in range(N):
        if i == j:
            continue
        comp = humans[j]
        if now[0] < comp[0] and now[1] < comp[1]:
            num += 1
    rst.append(num)

print(*rst)


