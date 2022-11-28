# 튜플 Tuple
# list와 유사한 데이터 타입 (리스트와 비교가 중요)
# 튜블 (순서O, 중복O, 수정X, 삭제X) => 불변 
# JS에서 const로 선언한 배열이랑 비슷한가보다...

# 선언
a = (1, 2, 3)
a1 = 1, 2, 3, 4
b = ()
c = tuple()
print(type(a1), type(b), type(c)) # tuple
d = (1,)
d1 = 1,
e = (1)
print(type(d), type(e)) # d = tuple, e = int
# 튜플의 원소가 1개일때는 ,를 찍어줘야 tuple로 인정된다.
f = (1, 2, 3, (6, 7))
print(f)

# 인덱싱
print(f[0])
print(f[-1][1])
print(f[3])

print(a + d)
print(type(list(d))) # list로 변환 가능

# 수정X
# f[3] = 0; # TypeError: 'tuple' object does not support item assignment

# 슬라이싱
print(f[0:2])
print(f[-1:])
print(f[::2])
print()
print()
print()

# 연산
print(f[3] + d)
print(d * 3)

g = (1, 2, 3, 4, 3, 5, 6, 3)

# 튜플함수
print(g.index(1))
print(g.count(3))
print()
print()
print()

# 팩킹, 언팩킹 (Packing, Unpacking)

# 팩킹 -> 묶는다, 튜플을 선언하는 것과 같음
h = (1, 2, 3, 4, 5, 6)
print(h[2])

# 언팩킹
(x1, x2, x3, x4, x5, x6) = h
print(x1, x2, x3, x4, x5, x6)
print(type(x1), type(x2), type(x3), type(x4), type(x5), type(x6)) # 모두 int가 나옴
# 구조분해 할당이랑 비슷한 것 같음
(title, name, age, hobby, email, phone) = h # 변수는 맘대로 정할 수 있는듯
# 언팩킹을 할 때 모든 원소를 다 해줘야 하는듯
print(title, name, age, hobby) # 프린트할 때는 문제없는 것 같음
print()
print()
print()

t = 1, 2, 3
a, b, c = t
print(t, 'packing')
print(a)
a, b, c = 4, 5, 6 # 그냥 할당만 하는듯? 튜플 선언과 언팩킹을 같이 하려는 듯
print(a, b, c, 'after unpacking')
print(a)
print(t, '값은 바뀌었나요?')
