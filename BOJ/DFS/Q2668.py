
N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
answer = set()


def dfs(first, second, num):
    first.add(num)
    second.add(arr[num])
    if arr[num] in first:
        if first == second:
            answer.update(first)
            return True
        return False
    return dfs(first, second, arr[num])


for i in range(1, N+1):
    if i not in answer:
        dfs(set(), set(), i)

print(len(answer))
print(*sorted(list(answer)), sep='\n')
'''
7
3
1
1
5
5
4
6

=>
3
1
3
5


7
3
1
1
6
5
4
6

=> 
5
1
3
4
5
6

7
3
1
1
7
5
4
6
=>
6
1
3
4
5
6
7
'''


