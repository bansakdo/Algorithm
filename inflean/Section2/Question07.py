import sys
import time

sys.stdin = open("input.txt", "rt")

start = time.time()
n = int(input())
prime = []
num = int(0)

# 내가 푼거

# 방법 1
'''
if n > 2:
    for i in range(2, n):
        flag = False
        for p in prime[:5]:
            if i % p == 0:
                flag = True
                break
        if flag:
            continue
        for j in range(2, i):
            if i % j == 0:
                if i != j:
                    break
        else:
            prime.append(i)
            print(prime)
            num += 1
    print(num)
elif n == 2:
    print(2)
elif n == 1:
    print(1)
# 20000 => 13초 이상
'''

# 방법2
'''
if n > 2:
    for i in range(2, n):
        for p in prime:
            if i % p == 0:
                break
        else:
            prime.append(i)
            num += 1
    else:
        prime.append(n)
        num += 1
    print(num)
elif n == 2:
    print(1)
elif n == 1:
    print(0)
# 100000 => 3.97초
# 200000 => 13.8 ~ 14.5초
'''

# 해설
# '''
ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)
# '''
print("time :", time.time() - start)

