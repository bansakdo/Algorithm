

T = int(input())

for _ in range(T):
    number = int(input())
    zero = [1, 0, 1]
    one = [0, 1, 1]

    if number <= 2:
        print(zero[number], one[number])
    else:
        while len(zero) <= number:
            zero.append(one[-1])
            one.append(zero[-1] + zero[-2])
        print(zero[-1], one[-1])





'''
1
2
3
5
8
13
21


'''