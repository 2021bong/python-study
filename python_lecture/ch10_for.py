# for문

# for in <collection>
#   <Loop body>

# range
# range(start, stop[, step])

for value in range(5): # 0 ~ 4
  print(value)
  
print('-----')
    
for value in range(1, 5): # 1 ~ 4
  print(value)
  
print('-----')

for value in range(1, 5, 2): # 1, 3
  print(value)

print('-----')



# 1부터 1000까지의 합
total = 0
for i in range(1, 1001):
  total += i
  
print(total)

# sum
print(sum(range(1, 1001)))
print(sum(range(1, 1001, 10))) # 1 ~ 1000 사이의 10의 배수만 더하기나 출력하기도 가능함



# Iterables 자료형
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ['bong','lee','kim']

for name in names:
  print(name)

for name in reversed(names):
  print(name)
  
a = 'hello world'

for char in a :
  print(char)
  
myInfo = dict(
  name = 'bong',
  age = '40',
  city = 'seoul'
)

for info in myInfo:
  print(info)  # 키출력
  print(myInfo[info]) # 밸류출력
  
for info in myInfo.values(): # 밸류출력
  print(info)



# 조건문과 반복문을 같이 쓰기
nickname = 'HelloWorld'

for n in nickname:
  if n.isupper(): # 대문자인지 판별
    print(n)
  else :
    print(n.upper()) # 대문자로 변경

print()
print()
print()



# break
for name in names:
  if name == 'lee':
    print(name)
    break
  else:
    print(name)
    
print()
print()
print()

# continue

mess = [1, 2, 'name', 3, 'age', 4, 5]

for v in mess:
  if type(v) is str: # is : 자료형을 계산할 때 사용
    continue # 조건문에 걸리면 continue가 실행되서 다음 v로 넘어감
  print(v)
    
    
# for - else
numbers = [1, 3, 32, 34, 68, 32,78, 100]

for num in numbers:
  if num == 100:
    print(num) # 100이면 실행
    break
else : # for와 같은 depth
  print('Not found 100') # 100없으면 실행
  
  
# 구구단 출력
for i in range(2, 10):
  for j in range(1, 10):
    print('{:3d}'.format(i * j), end='') # 숫자가 바뀔때만 줄바꿈을 하고 내부에선 end=''로 붙여줄거라서 3자리 정수로 출력
  print()
  

# reversed()도 형변환을 해줘야 값을 확인 할 수 있음
print(reversed('안녕하세요'))
print(list(reversed('안녕하세요')))