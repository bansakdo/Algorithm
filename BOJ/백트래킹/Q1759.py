
"""
def getCombVowel(cnt, val=""):
    global vowel
    rst = set()
    if cnt == 1:
        for v in vowel:
            if v not in val:
                rst.add("".join(sorted(val + v)))
        return rst
    else:
        for v in vowel:
            if v not in val:
                rst.update(getCombVowel(cnt - 1, val + v))
        return rst


def getCombCons(cnt, val=""):
    global consonant
    rst = set()
    if cnt == 1:
        for c in consonant:
            if c not in val:
                rst.add("".join(sorted(val + c)))
        return rst
    else:
        for c in consonant:
            if c not in val:
                rst.update(getCombCons(cnt - 1, val + c))
        return rst


L, C = map(int, input().split())

std_vowel = ('a', 'e', 'i', 'o', 'u')

vowel = []      # 모음
consonant = []  # 자음
answer = set()

input_data = list(input().split())
for d in input_data:
    if d in std_vowel:
        vowel.append(d)
    else:
        consonant.append(d)

for i in range(1, min(len(vowel) + 1, len(input_data) - 1)):
    v = list(getCombVowel(i))
    c = list(getCombCons(L - i))
    for _v in v:
        for _c in c:
            answer.add("".join(sorted(_v + _c)))

answer = sorted(answer)
for a in answer:
    print(a)

"""

from itertools import combinations

L, C = map(int, input().split())

std_vowel = ('a', 'e', 'i', 'o', 'u')

vowel = []      # 모음
consonant = []  # 자음
answer = set()

input_data = list(input().split())
for d in input_data:
    if d in std_vowel:
        vowel.append(d)
    else:
        consonant.append(d)

for i in range(1, min(len(vowel) + 1, len(input_data) - 1)):
    if L - i < 2:
        continue
    v = list(combinations(vowel, i))
    c = list(combinations(consonant, L - i))

    for _v in v:
        for _c in c:
            answer.add("".join(sorted(_v + _c)))

answer = sorted(answer)
print(len(answer))
for a in answer:
    print(a)
