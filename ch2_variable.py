#Chapter 02 - 2 : 변수 (Variable)

# 기본선언
# 간단한 선언은 예약어를 사용할 필요가 없는 것 같다. 짱이다....
n = 700
x = 50
angel = 1004

print(n)
print(x)
print(angel)

# 출력
# type(변수)를 사용하면 자료형을 파악할 수 있다.
print(type(n)) # <class 'int'>

# 동시 선언
x = y = z = 100
print(x, y, z) # 100, 100, 100

# 선언
var = 10
print(var, type(var))

# 재선언
var = 'not recommend in js'
print(var, type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력
# 뭔가.. C랑 비슷한것같다.. 메모리를 할당하고 값을 넣고 그 메모리 주소를 변수에 할당.. 부르면 그 값을 출력..! 역시 C는 근본이구나....

# 예 1)
print(300)
print(type(300))

# 예 2)
# n -> 777
n = 777
print(n, type(n))
m = n
# m -> 777 <- n

print(m, type(m),'과', n, type(n)) # 777 <class 'int'> 과 777 <class 'int'>

m = 7

print(m, type(m),'과', n, type(n)) # 7 <class 'int'> 과 777 <class 'int'>
# m에 n값의 메모리주소가 있었는데 그걸 버리고 7을 메모리에 저장한걸까..?

# *****(중요)******
# id(identity)확인 : 객체의 고유값 확인 

m = 100
n = 50

print(id(m), id(n)) # 4556494288 4556304208 <- 고유값 === id
print(id(m) == id(n)) # False

a = 1
b = 1
c = 1
d = 1
print(id(a), id(b), id(c), id(d)) # 4491131184 4491131184 4491131184 4491131184
# 같은 값을 불필요하게 여러번 저장할 필요는 없기 때문에 하나의 오브젝트로 생성함 (id가 같다) -> 같은 오브젝트를 참조한다.
# 파이썬은... 천재다......





# 다양한 변수 선언
# 네이밍으로 실력 판단 가능~ 네이밍을 잘하자~~~
# 카멜케이스 -> 메소드 선언
# 파스칼케이스 -> 언어를 따지지않고 클래스를 선언할 때 주로 사용
# 스네이크 -> 파이썬에서 많이 사용함 (변수 선언)

# 파이썬 예약어
# for
# as
# class
# except
# with
# assert
# finally
# yield
# break

# from
# False
# def
# if
# raise
# None
# del
# import
# return
# True

# elif
# in
# try
# and
# else
# if
# while
# lambda
# nonlocal
# not

# continue
# global
# pass