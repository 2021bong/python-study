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

# \** 비트단위(bitwise) 연산자
# ~(bitwise not) : (~ : tilde, 틸드라고 읽는다.)

# &(bitwise and) : (and, ampersand, 앰퍼센드라고 읽는다.) 

# |(bitwise or) : (or, vertical bar, 버티컬바, 파이프(pipe)연산자라고도 불리는 경우가 있다.)

# ^(bitwise xor) : (xor, circumflex/caret, 서컴플렉스/카릿), (C언어에서는 전혀 다른 배타적 논리합(xor, 서로 다를 때 1)의 의미를 가진다.)
# ^를 구체적으로 설명하자면, 두 장의 이미지가 겹쳐졌을 때 색이 서로 다른 부분만 처리할 수 있다.
# 배경이 되는 그림과 배경 위에서 움직이는 그림이 있을 때,
# 두 그림에서 차이만 골라내 배경 위에서 움직이는 그림의 색으로 바꿔주면 전체 그림을 구성하는 모든 점들의 색을 다시 계산해 입히지 않고 보다 효과적으로 그림을 처리할 수 있게 되는 것이다.
# 비행기 슈팅게임 등을 상상해보면 된다.

# <<(bitwise left shift), >>(bitwise right shift)

# 3항연산
# 3개의 요소로 이루어지는 3항 연산은
# "x if C else y" 의 형태로 작성이 된다.
# - C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
# - x : C의 평가 결과가 True 일 때 사용할 값
# - y : C의 평가 결과가 True 가 아닐 때 사용할 값
# 중첩도 가능하며 연산자 우선순위에 따라 실행되니 주의한다. 
# 예 : (a if a>b else b) if ((a if a>b else b)>c) else c
n1, n2, n3 = 3, -1, 5
print((n1 if n1 < n2 else n2) if ((n1 if n1 < n2 else n2) < n3) else n3)