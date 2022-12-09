# list 리스트
# 다른언어에서는 배열
# 자료구조뿐만 아니라 프로그래밍 언어에서 중요함
# 리스트 - 순서, 중복, 수정, 삭제를 허용하는 유일한 자료형

# 선언
# 빈 리스트
a = []
b = list()

c = [1, 2, 3]
print(len(c))

d = [1000, 'a', 1.1, True]
e = [[1, 2, 3], 100, ['a', 'b']]

# 인덱싱
print(e[0][1]+e[1], e[2][0])
print(e[-1][-1])

# 형변환
print(list(e[-1][-1]), type(list(e[-1][-1])))

# 슬라이싱
print(e[1:3])
print(c[:-1])
print(e[-1:])
print(d[1::2])
print()
print()
print()

# 리스트 연산
print(c + d)
print(c * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print('test'+str(c[0]))

# 값 비교
print(c)
print(c[:3])
print(c == c[:3])
print()
print()
print()

# Identity(id)
temp = c;
print(temp)
print(id(c))
print(id(temp))
print()

temp = c[1:2]
print(temp)
print(id(c))
print(id(temp))

# 리스트 수정, 삭제
c[1] = 10
print(c)
c = c + ['a','b']
print(c)
c = c[0:2] + ['a','b'] + c[2:]
print(c)
c[1:3] = [] # 빈 list를 넣으면 삭제와 비슷함. 하지만 삭제가 따로 있음.
print(c)
print()
print()
print()

d[1:2] = [1,2]
print(d) # [1000, 1, 2, 1.1, True]
d[1] = [1,2] # 인덱스 자체로 바꾸면 list 자체가 들어감
print(d) # [1000, [1, 2], 1.1, True]

f = [1, 2, 3, 4]
del f[2]
print(f)
print()
print()
print()

# 리스트 함수
g = [4, 2, 1, 3, 5, 2, 2, 6]

g.append(8) # == array.push() (JS)
print(g)
g.sort() # == array.sort() (JS)
print(g)
g.reverse() # == array.reverse() (JS)
print(g)
print(g.index(1),'==',g[1])
g.insert(2, 100) # list.insert(넣을 위치, 추가할 요소) == g.splice(2, 0, 100) (JS)
print(g)
g.remove(100) # list.remove(제거할 값)
print(g)
g.pop()
print(g) # == array.pop() (JS)
print(g.count(2)) # list.count(찾는값) : 찾는값이 몇개가 있는지 확인해줌
ex = [100, 1000]
g.extend(ex) # 확장, 뒤에 해당 list를 추가한다.
print(g)

# 삭제 : remove, pop, del

# 반복문 활용
while g:
  data = g.pop()
  print(data)