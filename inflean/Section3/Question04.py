import sys
sys.stdin = open("input.txt", "rt")

# 4번 문제. 두 리스트 합치기

# 내가 푼거
'''
size1 = int(input())
_list1 = [int(x) for x in input().split()]
size2 = int(input())
_list2 = [int(x) for x in input().split()]

rst = _list1
rst += _list2
rst.sort()
for x in rst:
    print(x, end=' ')
# .sort()는 nlog(n)번 반복하여 수행.
'''

'''
# n번 만 사용하여 정렬
size1 = int(input())
_list1 = [int(x) for x in input().split()]
size2 = int(input())
_list2 = [int(x) for x in input().split()]

rst = []
for i in range(size1 + size2 + 1):
    if len(_list1) == 0:
        rst += _list2
        break
    elif len(_list2) == 0:
        rst += _list1
        break
    elif _list1[0] < _list2[0]:
        rst.append(_list1[0])
        _list1.pop(0)
    elif _list1[0] > _list2[0]:
        rst.append(_list2[0])
        _list2.pop(0)
    elif _list1[0] == _list2[0]:
        rst.append(_list1[0])
        rst.append(_list2[0])
        _list1.pop(0)
        _list2.pop(0)
for x in rst:
    print(x, end=' ')
'''

# 해설
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0
c = []
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]
for x in c:
    print(x, end=' ')
