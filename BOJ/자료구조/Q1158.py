from collections import deque

N, K = map(int, input().split())
arr = deque(x for x in range(1, N+1))

rst = []
order = 0
while arr:
    order += 1
    if order % K == 0:
        rst.append(arr.popleft())
    else:
        arr.append(arr.popleft())

print("<{}>".format(str(rst)[1:-1]))




'''
9 2
1 2 3 4 5 6 7 8 9
2 4 6 8 1 5 9 7 3

10 10
1 2 3 4 5 6 7 8 9 10
10 1 3 6 


7 3
1 2 3 4 5 6 7
3 6 2 7 5 1 4


'''







