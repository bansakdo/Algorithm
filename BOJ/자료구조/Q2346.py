

'''
5
3 2 1 -3 -1
=> 1 4 5 3 2


6
3 -7 6 -3 1 -1
=> 1 4 6 5 2 3

6
3 2 6 -3 1 -1
=> 1 4 6 5 2 3

1
3

8
-1 5 -3 -4 6 7 3 1
=> 1 8 2 7 5 4 6 3

'''



# 2346번 문제. 풍선 터뜨리기

n = int(input())
bal = [int(x) for x in input().split()]
length = len(bal)
bal = list(enumerate(bal))
res = []
last = 0

while length > 1:
    # print(last, bal[last], bal)
    tmp = bal.pop(last)
    next_idx = last + tmp[1]
    res.append(tmp[0] + 1)
    length -= 1
    if next_idx < 0:
        next_idx = length - (abs(next_idx) % length)
    else:
        next_idx = (next_idx - 1) % length

    last = next_idx

res.append(bal[0][0] + 1)

print(*res)




