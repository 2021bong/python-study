# 문자열 밀기

# list.pop() : 맨 마지막 요소 삭제
# list.remove(값) : 원하는 요소 삭제

# append() : 맨 뒷자리에 추가
# insert(자리, 값) : 원하는 자리에 추가

def solution(A, B):
  if A == B :
    return 0
  i = 0
  list_a = list(A)
  while i < len(A):
    list_a.insert(0, list_a[len(list_a) - 1])
    list_a.pop()
    if ''.join(list_a) == B:
      return i + 1
    i += 1
  else :
    return -1
  
# print(solution('hello','ohell'))
# print(solution('apple','elppa'))
# print(solution('atat','tata'))
# print(solution('abc','abc'))

# 너무 기발한 다른 사람의 풀이
solution=lambda a,b:(b*2).find(a)
# B를 2번 곱한 문자열에서 A의 인덱스를 찾는다.
# 없으면 -1이 나올테고
# 같으면 0
# 있다면 해당 인덱스가 나오는데 그 인덱스는 몇번 밀었는지와 동일하다.
# 진짜 그냥 똑똑하다는 말밖에...............