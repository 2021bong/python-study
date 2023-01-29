# 유한소수 판별하기

# import math

# 최대 공약수
# def gcdRecursive(x, y):
#   if y == 0:
#     return x
#   else :
#     return gcdRecursive(x, x % y)
  
# 소수인지 판별하기
# def isPrime(num):
#       for i in range(2, math.floor(math.sqrt(num))+1):
#           if num % i == 0 :
#               return False
#       return True

# 소수 찾기
# def findPrimes(n):
#     primes = []
#     for i in range(2, n+1):
#         if isPrime(i):
#             primes.append(i)
#     return primes
  
# 소인수 찾기
# def factorize(n):
#     factors = []
#     primes = findPrimes(n)
#     for i in primes:
#         while (n % i == 0):
#             factors.append(i)
#             n = n // i
#     return factors

# 첫번째 풀이 (6, 7, 11, 20, 24, 25, 43, 45 케이스 실패)
# def solution(a, b):
#   gcd = int(gcdRecursive(a, b))
#   if (b % gcd != 0) and (gcd == a):
#     primeOfb = factorize(b)
#   else:
#     primeOfb = factorize(int(b / gcd))
#   for num in primeOfb:
#       if num != 2 and num != 5:
#           return 2
#   return 1



# 다른 사람 풀이 참고
# math에서 최대 공약수 구하는 함수를 import할 수 있다.
# b를 5나 2로 나눴을 때 나머지가 더 이상 0이 아니라면 while문을 빠져나올 것 이므로 사용이 적절하다. (이 부분을 이해를 못했다.)
# b를 나눌 때 /를 사용하면 float가 되고 //연산자를 사용하면 int가 되어서 //를 사용한 것 같다.
# while문을 돌려서 다 나누고 남은 b가 1이 아니라면 다른 소수가 있는 것이므로 2를 리턴하면 된다.

from math import gcd

def solution(a, b):
  gcdNum = int(gcd(a, b))
  if b % gcdNum == 0:
    b = int(b / gcdNum)
  while b%5 == 0:
    b/=5
  while b%2 == 0:
    b/=2
  if b == 1:
    return 1
  else:
    return 2

# 다른 사람 풀이 참고
# 아예 a, b를 나눠서 길이가 길면 무한소수일 확률이 높기 때문에 문자열의 길이로 계산한다.
# 10이나 16으로 통과했다는 답을 봤는데 1개 케이스씩 통과하지 못했다. (테스트 케이스가 추가되어서 그런듯)
def solution(a, b) :
  if len(str(a/b)) > 15:
    return 2
  else:
    return 1

# print(solution(7, 20)) # 1
# print(solution(11, 22)) # 1
# print(solution(12, 21)) # 2
# print(solution(12, 60)) # 1
# print(solution(25, 30)) # 2
# print(solution(12, 36)) # 2
# print(solution(3500, 500)) # 1
# print(solution(1, 16)) # 1
# print(solution(1, 32)) # 1
# print(solution(1, 512)) # 1
# print(solution(1, 11)) # 2
# print(solution(1, 17)) # 2
# print(solution(1, 30)) # 2
# print(solution(1000, 100)) # 1