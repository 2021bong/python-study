# chapter 3 숫자형

# !!! Run code를 하기 전에 파일 저장을 잊지말 것 !!!

# 파이썬 지원 자료형

# int : 정수
# float : 소수
# complex : 복소수
# bool : 불리언
# str : 문자열(시퀀스)
# list : 리스트(시퀀스)
# tuple : 튜플(시퀀스)
# set : 집합
# dict : 사전

# 데이터타입
str1 = "python"
bool = True
str2 = "Anaconda"
float1 = 10.0 # 10 == 10.0 (정수와 소수는 데이터 타입이 다름) float는 예약어가 아님
int1 = 7
list = [str1, str2] # list 는 []
dict = {
  "name" : "Code Kim",
  "age" : 60
} # dict 는 {}안에 key와 value
tuple1 = (1, 2, 3) # tuple은 ()
tuple2 = 1, 2, 3
# tuple은 괄호 없이 콤마로도 선언할 수 있다. 보통은 괄호를 사용해서 정확하게 적어주는 것이 좋다.
set = {1, 2, 3} # set은 {}

# type()으로 자료형의 타입을 확인해 볼 수 있다.

print(type(dict))
print(type(tuple1))
print(type(tuple2))
print(type(set))
print()
print()
print()

# ------------------------------------------------------------------------------------

# 숫자형 연산자

# +
# -
# *
# /
# // : 몫을 반환 , js에서는 나눗셈을 하고 몫을 알아서 정수처리 해줘야됐는데 파이썬은 몫을 계산해주는 연산자가 있다..!
# %
# abs(x) : 절대값
# pow(x, y) == x ** y : x의 y제곱

# 정수

i = 77
i2 = -14
bi = 7777777777777777777777777777777777777777777777 # 다른 언어에서는 bigint는 데이터 타입을 따로 처리해줘야되는데 파이썬은 그냥 넣으면 된다.
print(i, i2, bi , sep='\n')

# 실수
f = 1.234
f2 = 3.14141414
f3 = -0.9
f4 = 4 / 3
print(f, f2, f3, f4, sep='\n')
print()
print()
print()

# 연산
i1 = 100
i2 = 50
big_int1 = 100000000000000000000000000000
big_int2 = 101010101010101010101010101010
f1 = 0.5
f2 = 1.5

print(i1 + i2)
print(big_int2 - big_int1)
print(f1 - f2)
print(i2 - f2) # 서로 다른 형을 계산하면 형변환이 이뤄진다.
print(i2 // f1)
print(big_int2 % big_int1)
print()
print()
print()

# 형변환 함수
a = 3.
b = 6
c = .7
d = 12.0

print(type(a),type(b),type(c),type(d))

# float이나 int같은 함수와 동일한 이름의 변수가 있으면 에러가 난다.
print(int(a),float(b),int(c),int(d))
print(int(True)) # True == 1 , False == 0
print(float(False))
print(complex(3))
print(complex('3')) # 문자를 넣어도 내부적으로 문자를 숫자로 변경 후 실행해준다.
print(complex(True))
print(complex(False))
print()
print()
print()

# 수치연산 함수
print(abs(-7)) # 절대값
x,y = divmod(100, 25) # 100을 8로 나누고 x와 y에 할당, 나눈 다음에 몫과 나머지를 x와 y에 담을 수 있다. (자주 쓰임)
print(x, y)
print(pow(2, 3))
print(2 ** 3)
print()
print()
print()

# 외부 모듈
import math # 좀 더 공학적인 수치 계산을 할 때는 외부 패키지를 가져와서 사용할 수 있다.

print(math.pi)
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수를 반환
print(math.floor(1.23455))