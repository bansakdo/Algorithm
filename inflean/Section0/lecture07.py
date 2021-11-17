# 문자열과 내장함수

msg = "It is Time"

print(msg)
print(msg.upper())          # 대문자화
print(msg.lower())          # 소문자화

tmp = msg.upper()
print(tmp)
print(tmp.find('T'))        # T를 찾아서 index 출력. 1
print(msg.find('T'))        # 6
print(tmp.count('T'))       # T의 숫자 센 후 출력. 2
print(msg[:2])              # slice. 처음부터 index 2 전까지 잘라서 출력
print(msg[3:5])             # index 3부터 5 전까지 출력. index에는 공백 포함
print(len(msg))             # 문자열 길이 출력
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():         # 대문자인지 확인 후 boolean 리턴
        print(x, end=' ')
print()

for x in msg:
    if x.islower():         # 소문자인지 확인 후 boolean 리턴
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():         # 알파벳인지 확인
        print(x, end=' ')
print()

tmp = 'AZ'
for x in tmp:
    print(ord(x))           # ord: 아스키 넘버 출력. A: 65, Z: 90

tmp = 'az'
for x in tmp:
    print(ord(x))           # ord: 아스키 넘버 출력. a: 97, z: 122

tmp=65
print(chr(tmp))             # 해당 숫자에 해당하는 아스키코드 출력









