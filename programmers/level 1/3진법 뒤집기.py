# 3진법 뒤집기

# int(문자열, n진법) -> 문자열은 n진법이라서 10진법 int로 바꾸겠다는 뜻

def solution(n):
  base = 3
  temp = ''
  while n:
    temp += str(n % base)
    n //= base
    
  return int(temp, 3)

# print(solution(45))
# print(solution(125))