# 클래스 class

# 객체 지향 프로그래밍 (OOP)
# 재사용이 용이 (개선, 수정, 버그)

# 클래스 and 인스턴스 차이
# 선언
# class Cat: #object 상속
# class Cat():
# class Cat(object):


class Cat:
  # 클래스 속성 # 클래스 변수
  animal = '고양이'
  
  # 초기화/인스턴스 속성
  def __init__(self, species,name, age):
    self.name = name
    self.age = age
    self.species = species
  # self == (JS) construnctor 안의 this ?
    
lussian_blue = Cat('러시안블루','루이', '10')
print(dir(lussian_blue))

# 네임 스페이스 : 객체를 인스턴스화 할 때 저장된 공간
print(lussian_blue.__dict__)

# 클래스 변수 : 직접 접근 가능, 공유
print(Cat.animal)
print(lussian_blue.animal)
if Cat.animal == '고양이':
  print(Cat.animal)

# 인스턴스 변수 : 객체마다 별도 존재
bengal = Cat('벵갈', '호야', '3')
print(lussian_blue.name)
print(bengal.name)

# 인스턴스 속성 확인
print('name : {}, age : {}, species : {}'.format(lussian_blue.name, lussian_blue.age, lussian_blue.species))

# self
class selfTest:
  def func1():
    print('call func1')
  def func2(self):
    print('call func2')
    
f = selfTest()
# f.func1() # 에러
f.func2() # def func2(self자리에 f가 들어감)

# 호출하는 방법 -> selfTest.func1()
selfTest.func1()
# selfTest.func2() # 반면에 func2를 이렇게 호출하면 에러가 남
selfTest.func2(f) # 이렇게하면 호출 가능

# func1 -> 클래스 메소드
# func2 -> 인스턴스 메소드

print()
print()
print()

class WareHouse:
  stock_num = 0
  
  def __init__(self, name):
    self.name = name
    WareHouse.stock_num += 1
  
  # 객체가 사라질 때 호출되는 메소드
  def __del__(self):
    WareHouse.stock_num -= 1
    
desk = WareHouse('desk')
chair = WareHouse('chair')

print(desk.__dict__)
print(chair.__dict__)
print(WareHouse.__dict__)
print(desk.stock_num)

print(WareHouse.stock_num)
del chair # 객체를 삭제해 __del__ 메소드가 실행됨
print(WareHouse.stock_num)

class Dog:
  animal = '개'
  
  def __init__(self, species,name, age):
    self.name = name
    self.age = age
    self.species = species
    
  def info(self):
    return '{}는 {}살이에요.'.format(self.name, self.age)
  
  def snack(self, snack):
    return '{}가 제일 좋아하는 간식은 {}에요.'.format(self.name, snack)
  
kkukku = Dog('시베리안 허스키', '꾸꾸', '5')
print(kkukku.info())
print(kkukku.snack('고구마'))