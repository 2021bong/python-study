# function

# 정의
# def function_name(parameter):
#       ...

def func1(name):
  print('Hi', name)

def func2(name):
  return 'Hi ' + name
  
func1('bong')
greeting = func2('bong')
print(greeting)

# 다중 반환
def func3(num):
  n1 = num * 10
  n2 = num * 20
  n3 = num * 30
  return n1, n2, n3

x, y, z = func3(1)
print(x, y, z)

def func_tuple(num):
  n1 = num * 10
  n2 = num * 20
  n3 = num * 30
  return (n1, n2, n3)

t = func_tuple(1)
print(t, type(t), list(t))

def func_list(num):
  n1 = num * 10
  n2 = num * 20
  n3 = num * 30
  return [n1, n2, n3]

l = func_list(1)
print(l, type(l))

def func_dict(num):
  n1 = num * 10
  n2 = num * 20
  n3 = num * 30
  return {'n1':n1, 'n2':n2, 'n3':n3}

d = func_dict(1)
print(d, type(d), d.get('n2'), d.items(), d.keys())

# 중요
# \*args, **kwargs 아스타 언팩킹 가변인자
# (JS) function(...rest) 같은 건가..?
def func4(*args): # 리스트나 튜플형태일 때 사용
  for i, v in enumerate(args):
    print('i :',i,' v :',v)
    
func4(1, 2, 3)
func4([1, 2, 3]) # i : 0  v : [1, 2, 3]

def func5(**kwargs): # 딕셔너리 형태로 키와 밸류를 넘길 때 사용
  for v in kwargs.keys():
    print(v, ':',  kwargs[v])

# 왜 딕셔너리 자체를 넘기는 것도 아닌 이런 형태를...???
func5(name='bong',age=60,hobby='python')
# print(type(name='bong')) # 이렇게하면 에러나잖아...

# 함수중첩
def nest(num):
  def inside(num):
    print(num)
  print('run nest')
  inside(num + 100)

nest(100)

# lambda(람다)
# 장점 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수 -> 메모리 초기화
# 남발 시 가동성 오히려 감소
# 익명함수이며 함수의 인자로 넘길 수도 있다.

# 일반함수할당
def mul_func(x, y):
  return x * y

mul_func_var = mul_func
print(mul_func_var(2, 5))

# 람다함수할당
xylambda = lambda x, y : x * y
print(xylambda(2, 5))

# 함수를 인자로 넘길 때
def func6(x, y, func):
  print(x * y * func(10, 10))
  
func6(2, 5, lambda x, y : x * y)
func6(2, 5, xylambda)
func6(2, 5, mul_func_var)