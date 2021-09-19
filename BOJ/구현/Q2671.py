
# engine_pattern = "(100~1~|01)~"       # 엔진 패턴
input_string = str(input())

N = len(input_string)
splitter = [i for i in range(N) if input_string[i] == '1']
isSubmarine = False
last = -1
if input_string[:2] == '01':
    last = 2
for i in range(1, len(splitter)):
    s_slice = input_string[splitter[i-1] + 1:splitter[i] + 1]
    if s_slice == '01' and last != -1:
        last = 2
        continue

    s_slice = input_string[splitter[i-1]:splitter[i] + 1]
    if s_slice == '11' and (last == 1 or last == 11 or (input_string[splitter[i-1]-1:splitter[i]+2] == '0110')):
        last = 11
        continue
    s_size = len(s_slice)
    if s_size >= 4:
        s_compare = '100' + ('0' * (len(s_slice) - 4)) + '1'
        if s_slice == s_compare:
            last = 1
            if input_string[splitter[i-1]-1] == '0':
                break
    else:
        break
else:
    isSubmarine = True

if input_string[0] == '0' and (N == 1 or (N >= 2 and input_string[:2] != '01')):
    isSubmarine = False
elif input_string[0] == '1' and N < 4:
    isSubmarine = False
elif input_string[-1] == '0':
    isSubmarine = False


if isSubmarine:
    print("SUBMARINE")
else:
    print("NOISE")




