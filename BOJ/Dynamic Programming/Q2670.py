N = int(input())
arr = list(float(input()) for _ in range(N))
for i in range(1, N):
    arr[i] = max(arr[i], arr[i] * arr[i - 1])
print('%0.3f' % max(arr))

'''
8
1.1
0.7
1.3
0.9
1.4
0.8
0.7
1.4

=> 1.638

8
1.1
0.7
1.3
0.9
1.4
1.7
0.9
2.0

=> 5.012

8
1.1
9.9
0.0
0.9
1.4
0.0
0.7
1.4

=> 10.89

8
2.2
3.0
4.0
0.2
1.7
0.9
1.4
1.1

=> 26.4
'''
