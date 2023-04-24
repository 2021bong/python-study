# 예외 (Exception)

# 예측가능한 예외(비밀번호가 틀렸다..!)가 있고, 예측하지 못한 예외(하드디스크가 꽉 차버렸다..!)가 있을 수 있다.
# 하드웨어적으로 발생하는 에러
# 예외처리를 잘해야 처음과 끝이 내가 예상한대로 잘 작동하는 프로그램을 만들 수 있다.

# 문법적으로 예외가 없어도 코드 실행 단계에서 발생하는 예외도 중요하다.
# 1. 예외는 반드시 처리한다.
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외를 무시해서 예외가 쌓인다면 미래에 좋지 않은 결과를 가져온다.

# 예외 없는 것을 가정하고 프로그램 작성한다. -> 런타임 예외 발생 시 예외 처리를 권장한다. (EAFP)
# EAFP : It’s Easier to Ask Forgiveness than Permission. 허락을 구하는 것보다 용서를 구하는 것이 쉽다.

# SyntaxError : 문법 에러
# TypeError : int + str
# NameError : 없는 변수 호출
# IndexError : 잘못된 index 접근
# ValueError : 잘못된 value 접근
# KeyError : 없는 key 접근 => get() 메서드를 쓰는게 안전하다. 없으면 None을 가져 옴.
# FileNotFoundError : 존재하지 않는 파일 접근
# AttributeError : 모듈, 클래스에 잘못된 속성 사용 -> import time을 하고 멋대로 time12314()라는 메서드를 호출하면 에러 발생
# ZeroDivisionError : 100 / 0 <- 불가



# try :에러가 발생할 가능성이 있는 코드 실행
# except 에러명 : 여러 개 가능 (에러1, 에러2)
    # except error1 :
    # except error2 :
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

# 에러 핸들링 1
name = ['bong', 'lee', 'kim']
try:
  z  = 'kim'
  x = name.index(z)
  print("{}'s index : {}".format(z, x))
  # a = 'choi'
  # b = name.index(b)
  # print("{}'s index : {}".format(a, b))
except NameError: # 예측하고 있는 에러와 except 옆 에러를 맞춰주지 않으면 기존에 발생하던대로 에러가 발생함
  print("There's no vlaue in name") # 같은 타입의 에러를 지정해줘야 실행됨
else: # 에러가 발생하지 않으면 실행됨
  print('Good!')
finally:
  print('Python error handling1')
print()

# 에러 핸들링 2
name = ['bong', 'lee', 'kim']
try:
  a = 'choi'
  b = name.index(b)
  print("{}'s index : {}".format(a, b))
except: # 에러가 발생하면 다 잡는다. 하지만 어떤 타입의 에러인지 확인 불가능
  print("Error!!!!!!!!!")
else:
  print('Good!')
finally:
  print('Python error handling2')
print()

# 에러 핸들링 3
name = ['bong', 'lee', 'kim']
try:
  a = 'choi'
  b = name.index(b)
  print("{}'s index : {}".format(a, b))
except Exception as e: # 제일 상위 에러라서 로그도 찍으면서 다 잡을 수 있음
  print(e) # error 출력
  print('super Exception')
else:
  print('Good!')
finally:
  print('Python error handling3')
print()



# 에러 던지기
try:
  fruit = 'apple'
  if fruit == 'orange':
    print('orange ! yummy !')
  else:
    raise ValueError
except ValueError:
  print('apple is not allowed')
else:
  print('for tasty fruit...')