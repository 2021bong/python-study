# 최대공약수와 최소공배수

# gcd(최대공약수)와 lcm(최고공배수)는 math라이브러리를 통해서도 가능하다

# import math
# def solution(n, m):
  # return [math.gcd(n,m), math.lcm(n,m)]

# 파이썬 유클리드 호제법
# while m > 0:
#   n, m = m, n % m
# return n

# swap  : temp 없이 두 변수의 값을 바꿀 수 있음
# a, b = b, a

# 최소공배수
# 두 수를 곱한 수 / 최대공약수

def gcd(n,m):
    while m > 0:
      n, m = m, n % m
    return n
  
def solution(n, m):
    return [gcd(n,m),int(n * m / gcd(n, m))]
  
# print(solution(3,12))
# print(solution(2,5))