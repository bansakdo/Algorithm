
# Divide And Conquer
def dac(a, b):
    if b == 1:
        return a % C

    tmp = dac(a, b // 2)
    if b % 2 == 0:
        return tmp * tmp % C
    else:
        return tmp * tmp * a % C


A, B, C = map(int, input().split())

print(dac(A, B))



