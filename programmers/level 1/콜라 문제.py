# 콜라 문제

# 콜라를 받기 위해 마트에 주어야 하는 병 수 : a
# 빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수 : b
# 상빈이가 가지고 있는 빈 병의 개수 : n

def solution(a, b, n):
  coke = 0
  while n // a > 0: # 다른 사람 풀이 -> 연산을 1번만 하는 while n >= a 이 조건이 더 좋을 것 같다. (나는 2번함.)
    coke += (b * (n // a))
    n = (n % a) + (b * (n // a))
  return coke

# print(solution(2, 1, 20))
# print(solution(3, 1, 20))
# print(solution(5, 3, 21)) # 27