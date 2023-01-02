# 유한소수 판별하기

import math

# 최대 공약수
def gcdRecursive(x, y):
  if y == 0:
    return x
  else :
    return gcdRecursive(x, x % y)
  
# 소수인지 판별하기
def isPrime(num):
      for i in range(2, math.floor(math.sqrt(num))+1):
          if num % i == 0 :
              return False
      return True

# 소수 찾기
def findPrimes(n):
    primes = []
    for i in range(2, n+1):
        if isPrime(i):
            primes.append(i)
    return primes
  
# 소인수 찾기
def factorize(n):
    factors = []
    primes = findPrimes(n)
    for i in primes:
        while (n % i == 0):
            factors.append(i)
            n = n // i
    return factors

def solution(a, b):
  gcd = int(gcdRecursive(a, b))
  if (b % gcd != 0) and (gcd == a):
    primeOfb = factorize(b)
  else:
    primeOfb = factorize(int(b / gcd))
  for num in primeOfb:
      if num != 2 and num != 5:
          return 2

  return 1

print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))