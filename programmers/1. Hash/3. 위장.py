
# 3. 위장

'''

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
=> 5

[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
=> 3


'''
'''
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
answer = 1

num = len(clothes)
apparel = dict()
for i in range(num):
    item = clothes[i]
    dict_item = apparel.get(item[1], 0)
    dict_item += 1
    apparel[item[1]] = dict_item

type = len(apparel.keys())
for x in apparel.values():
    answer *= (x + 1)
answer -= 1
print(answer)
'''
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
answer = 1
from collections import Counter
from functools import reduce

cnt = Counter([kind for name, kind in clothes])
print(cnt)
answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 2) - 1
print(answer)


