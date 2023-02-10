# module (모듈)
# 재사용이 가능하게 필요한 기능을 구현해놓은 것
# 함수, 변수, 클래스 등 파이썬 구성 요소들을 모아놓은 파일

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def power(x, y):
  return x ** y

# print(add(2, 1))
# print(subtract(2, 1))
# print(multiply(2, 2))
# print(divide(2, 1))
# print(power(2, 3))

# 다른 파일에서 import를 하면 자동으로 실행되는 코드들(print)을 선택할 수 있다.
# __name__ : 실행되는 위치가 이 파일이 아니고 다른 파일일 경우에는 실행되지 않음 == 외부에서는 실행되지 않음
# 보통 모듈이 어떻게 작동하는지 보여주기 위한 샘플들을 __main__에 작성한다.
if __name__ == '__main__':
  print('__main__')
  print(add(2, 1))
  print(subtract(2, 1))
  print(multiply(2, 2))
  print(divide(2, 1))
  print(power(2, 3))