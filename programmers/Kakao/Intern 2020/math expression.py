from itertools import permutations


def solution(expression):
    answer = 0
    ops = ['*', '+', '-']
    ops_perm = permutations(ops)

    nums = []
    exp = []

    last = 0
    for i, x in enumerate(expression):
        if i == len(expression) - 1:
            nums.append(int(expression[last:]))
        if str.isdigit(x):
            continue
        exp.append(x)
        nums.append(int(expression[last:i]))
        last = i + 1

    for ops_order in ops_perm:

        c_exp = exp.copy()
        c_nums = nums.copy()

        for op in ops_order:
            exp_idxs = [x for x, y in enumerate(c_exp) if y == op]
            i = 0
            for exp_idx in exp_idxs:
                exp_idx -= i
                c_exp.pop(exp_idx)
                num1, num2 = c_nums.pop(exp_idx), c_nums.pop(exp_idx)
                if op == '*':
                    val = num1 * num2
                elif op == '+':
                    val = num1 + num2
                elif op == '-':
                    val = num1 - num2
                c_nums.insert(exp_idx, val)
                i += 1

        answer = max(answer, abs(c_nums[0]))

    return answer



# expression = "100-200*300-500+20"
expression = "50*6-3*2"
print(solution(expression))