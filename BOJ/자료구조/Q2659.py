
def sol(num):
    lowest = num
    for _ in range(3):
        num = (num % 1000) * 10 + num // 1000
        lowest = min(lowest, num)
    return lowest


num = int("".join(map(str, input().split())))
num = sol(num)
cnt = 0

for i in range(1111, num + 1):
    if sol(i) == i:
        cnt += 1
        print(i)
print(cnt)



