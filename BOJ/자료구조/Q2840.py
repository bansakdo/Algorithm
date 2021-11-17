
n, k = map(int, input().split())
circle = ['?'] * n

for i in range(k):
    spin = input().split()
    s = int(spin[0]) % n
    s_char = str(spin[1])

    circle = circle[-s:] + circle[:-s]
    if circle[0] == '?':
        if s_char in circle:
            print('!')
            break
        circle[0] = s_char
    elif circle[0] == s_char:
        continue
    else:
        print('!')
        break
else:
    print("".join(circle))


'''
P C A S

4 6
2 P
1 S
8 S
6 C
3 A
6 P


A B C D E F

6 4
3 D
2 B
1 A
1 A




'''