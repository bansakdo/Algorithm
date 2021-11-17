'''






'''

# 1269번 문제. 대칭 차집합


'''
n = list(map(int, input().split()))
setA = list(map(int, input().split()))
setB = list(map(int, input().split()))
common = 0

# setA.sort()
# setB.sort()
j = 0
for i in range(n[0]):
    for k in range(j, n[1] - common):
        if setA[i] == setB[k]:
            common += 1
            j = k
            setB.pop(k)
            break

print(n[0] + n[1] - 2 * common)
'''

n = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len(a-b) + len(b-a))









