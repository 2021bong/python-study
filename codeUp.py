# 16진수
n = 5
print('%x'%n) # 16진수 소문자
print('%X'%n) # 16진수 대문자

# 8진수
print('%o'%n)
print()

# 유니코드
s1 = 'A'
print(ord(s1)) # == str.charCodeAt() (JS)
s2 = 65
print(chr(s2)) # == str.fromCharCode() (JS)

# 부호를 바꿔서 출력하기
n = 5
print(-n)

# 문자 여러번 출력하기
n = 1
s = 'Hello'
print(s * n)
print()

# format을 이용한 소수점 자리 수 자르기 : format(num, '.num(자릿수)f')
f = 0.2345
print(format(f, '.1f'))
print(format(f, '.2f'))
print(format(f, '.3f'))

# 비트시프트
# 컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에,
# 2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
# 지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,

# 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
# 오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,
# 가장 오른쪽에 있는 1비트는 사라진다.
# python에서 실수 값에 대한 비트시프트 연산은 허용되지 않고 오류가 발생한다.

n = 10
print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

# bool() == !! (JS)
m = '10'
print(bool(n))
print(bool(m))

# 참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or, 배타적 논리합) 연산이라고도 부른다.
a = True
b = False
print((a and (not b)) or ((not a) and b))
