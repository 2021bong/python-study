# 집합(Set)

# 순서 X, 중복 X, 추가 O, 삭제 O
# 자바스크립트 new Set 객체가.. 집합이었구나...

# 선언
a = set()
print(type(a)) # <class 'set'>

b = set([1, 2, 3, 4])
print(b)
print()
print()
print()

c1 = {1, 1, 1, True, 'a', 8}
cTrue = { True, 'a', 8, 1, 1, 1}
# {}괄호를 사용해서 선언하고 key가 없으면 집합(set) 자료형

print(c1) # {8, 1, 'a'}
print(cTrue) # {8, True, 'a'}
print(len(c1))# 3 , 1 == True 라서 중복을 삭제해서...???? 먼저 온 값을 남기고 뒤에 있는 값을 날리는 것 같음..
print(len(cTrue)) # 3

d = {1, 2, 3, 4, 4, 4}
print(2 in d) # in 연산자도 사용 가능
print()
print()
print()



# 튜플 변환(set -> tuple)
t = tuple(d)
print(t)
print(type(t), t[1], t[2:3])

e = {1, 2, 3, 4}

# 리스트 변환(set -> list)
l = list(e)
print(l)
print(type(l), l[2], l[2:3])
print()
print()
print()



# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5])
s2 = set([7, 8, 3, 4, 5])

# 교집합
print(s1 & s2) # & 
print(s1.intersection(s2)) # intersection()

#합집합
print(s1 | s2) # | 
print(s1.union(s2)) # union()

#차집합
print(s1 - s2) # -
print(s1.difference(s2)) # difference



#중복 원소 확인
print(s1.isdisjoint(s2)) # is"dis"joint : 교집합이 있으면 False 없으면 True가 나옴

# 부분 집합 확인
print(s1.issubset(s2)) # s1은 s2의 부분 집합이냐 s1 < s2
print(s1.issubset(s2)) # s1은 s2를 포함하냐
print()
print()
print()

a1 = {1, 2, 3}
a2 = {2, 3}

print(a1.issubset(a2))
print(a2.issubset(a1))
print(a1.issuperset(a2))
print(a2.issuperset(a1))
print()
print()
print()



# 추가 & 제거
f = set([1, 2, 3, 4, 5])

f.add(6) # add 
f.remove(1) # remove -> 없는 값을 지우려고 하면 에러가 발생 (예외 발생 O)
# f.remove(0)
f.discard(2) # discard -> 없는 값을 지우려고 해도 에러 발생 X, 추천 (예외 발생 X)
f.discard(0)
print(f)

f.clear() # clear 전부 다 삭제
print(f)

# 리스트와 딕셔너리도 clear() 사용 가능
list = [1, 2, 3]
print(list)
list.clear()
print(list)

dic = dict(name = 'bong', age = 40)
print(dic)
dic.clear()
print(dic)

# tuple은 안됨
# tuple = (1,)
# print(tuple)
# tuple.clear()
# print(tuple)