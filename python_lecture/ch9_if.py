# 파이썬 제어문 - if

# Truthy : 0이 아닌 수, 문자열, 리스트, 튜플
# Falsy : 0, '', [], (), {} ...

# 들여쓰기 중요!
# if
if True:
  print('true1')
  
if False and '':
  print('false1')
  
# if else
if False:
  print('false2')
else :
  print('true2')
  
# 관계 연산자
# >, >=, <, <=, ==, !=

# 논리 연산자
# and, or, not
if (not False):
  print('not false')
# 파이썬은 || 나 ?? 가 뭘까..?
print()
print()
print()

# 연산자 우선순위
# 산술 > 관계 > 논리
print(3 + 1 != 2 + 1 and 1 + 1 != 2 + 1)

# 다중 조건문
def getGrade(num):
  if num >= 90:
    return 'A'
  elif num >= 80:
    return 'B'
  elif num >= 70:
    return 'C'
  else :
    return 'D'
print(getGrade(85))
print()
print()
print()

# in, not in
list = [1, 2, 3]
print(1 in list)
print(5 in list)
print(1 not in list)
print(5 not in list)
print()
print()
print()

dic = dict(name = 'bong', grade='A', city='seoul')
print("name" in dic)
print("seoul" in dic)
print("seoul" in dic.values()) # values()를 호출하면 해당 딕셔너리의 값 중에 있는지 확인한다.