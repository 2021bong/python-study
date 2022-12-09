# dictionary 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 (순서 X, 키 중복 X, 수정 O, 삭제 O)

# 선언
user1 = {'name': 'bong', 'age': 45} # json처럼 키도 문자열로 해줘야한다.
user2 = {
  'name': 'bong',
  'age': 45
} # 가독성을 위한 줄바꿈&들여쓰기도 가능
grade_score = {1: 'a', 2: 'a', 3: 'f'} # 숫자도 key가 될 수 있다.
a = {'arr':[1, 2, 3]} # key가 있다면 값은 어떤 자료형이던 들어올 수 있다.

# 이렇게도 가능
b = dict([
  ('name','bong'),
  ('age',45),
]);

c = dict(
  name = 'bong', # 이렇게하면 Key를 문자열로 넣지 않아도 됨. 
  age = 45
)
# key를 문자열로 적어줘야한다면 이게 제일 편한 방법일듯 **선생님의 추천 방법**

print(user1, type(user1))
print(user1['name'], b['age'],c['name']) # 왜 대체 불편하게 문자열을........
print(user1.get('name'))

# print(user1['name1']) # 해당 키가 없기 때문에 에러 발생
print(user1.get('name1')) # 해당 키가 없으면 None으로 처리 **더 많이 씀**

print(grade_score[1]) # 숫자로 된 key도 같음
print(grade_score.get(3))

# 딕셔너리 추가
c['address'] = 'seoul'
print(c)
# 딕셔너리 수정
c['age'] = 30
print(c)
print(len(c))
print()
print()
print()

# 딕셔너리 함수 (반복문에서 사용 가능)
# dict_keys
# dict_values
# dict_items
print(c.keys()) # Object.keys(obj) (JS)
print(c.values()) # Object.values(obj) (JS)
print(c.items()) # Object.entries(obj) (JS) 위에서 b와 같은 형태를 반환함
print(list(c.keys()), list(c.values()), list(c.items()), sep='\n') # list로 형변환을 해서 사용할 수 있다.
print(list(c.items())[0], list(c.items())[1], list(c.items())[2])
print()
print()
print()

print(c.pop('name')) # 해당 키와 밸류를 삭제, 자체를 프린트하면 해당 값을 반환
print(c) # 그리고 딕셔너리를 확인해보면 삭제되어있음.
print(user1.pop('age'))
print(user1)
print(grade_score.pop(3))
print(grade_score)

e = dict(
  name = 'bong',
  age = 45,
  address = 'seoul',
  blood = 'O',
  mbti = 'ENFP'
)
print()
print(e.popitem()) # 임의의 값을 꺼내옴, 그런데 뭔가 선언한 순서 뒤부터 꺼내오는 느낌... 순서가 없으니까 그냥 우연일듯..
print(e)
print(e.popitem())
print(e)
print(e.popitem())
print(e)
print(e.popitem())
print(e)
print(e.popitem())
print(e) # 다 꺼내면 빈 딕셔너리가 됨
# print(e.popitem())
print(e) # KeyError: 'popitem(): dictionary is empty' / 더 꺼내면 에러 발생
print()
print()
print()

# in 연산자 : 키를 포함하고 있는지 확인
print('birth' in user2)
print('name' in user2)
print('age' in user2)

# dict.update() : 딕셔너리 값을 수정하거나 키&값을 추가할 수 있다.
print(user2)
user2.update(age=100)
temp = {'address' : 'seoul'}
user2.update(temp)
print(user2)
