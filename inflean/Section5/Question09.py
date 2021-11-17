import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

# 9번 문제. 아나그램

# 내 풀이
'''
word_1 = deque(input())
word_2 = deque(input())

dict_1 = dict()
dict_2 = dict()

for i in range(len(word_1)):
    if word_1[i] in dict_1:
        dict_1[word_1[i]] += 1
    else:
        dict_1[word_1[i]] = 1

for i in range(len(word_2)):
    if word_2[i] in dict_2:
        dict_2[word_2[i]] += 1
    else:
        dict_2[word_2[i]] = 1

if dict_1 == dict_2:
    print("YES")
else:
    print("NO")
'''

# 해설
'''
a = input()
b = input()

str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
'''

# 해설2 (개선코드)
'''
a = input()
b = input()
sH = dict()

for x in a:
    sH[x] = sH.get(x, 0) + 1

for x in b:
    sH[x] = sH.get(x, 0) - 1

for x in a:
    if sH.get(x) > 0:
        print("NO")
        break
else:
    print("YES")
'''

# 해설3 (리스트 사용)

a = input()
b = input()
str1 = [0]*52
str2 = [0]*52

for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1
    else:
        str1[ord(x) - 71] += 1
for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")

