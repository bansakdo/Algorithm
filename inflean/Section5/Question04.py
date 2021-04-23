import sys

sys.stdin = open("input.txt", "rt")


# 4번 문제. 후위식 연산

# 내 풀이
'''
q = list(str(input()))
stack = []
op = ['+', '-', '*', '/']

for x in q:
    if op.__contains__(x):
        b = int(stack.pop())
        a = int(stack.pop())

        if x == '+':
            rst = a + b
        elif x == '-':
            rst = a - b
        elif x == '*':
            rst = a * b
        elif x == '/':
            rst = a / b

        stack.append(rst)
    else:
        stack.append(x)

print(stack[0])
'''

# 해설
a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        elif x == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 / n1)
print(stack[0])



