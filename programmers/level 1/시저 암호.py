# 시저 암호

def solution(s, n):
    answer = []
    for char in s:
      if char == ' ':
        answer.append(' ')
      else:
        if ord(char) >= 65 and ord(char) <= 90:
          if ord(char) + n > 90:
            answer.append(chr((ord(char) + n) - 26))
          else:
            answer.append(chr(ord(char) + n))
        else:
          if ord(char) + n > 122:
            answer.append(chr((ord(char) + n) - 26))
          else:
            answer.append(chr(ord(char) + n))
    return ''.join(answer)
    
# print(solution("AB", 1))
# print(solution("z", 1))
# print(solution("a B z", 4))
# print(solution("AZaz", 25))

# ord() 문자 -> 아스키
# chr() 아스키 -> 문자
# A : 65, Z : 90
# a : 97, z : 122



# 다른 사람의 풀이
# 굳이 ' '에 대한 케이스를 추가하지 않고 문자열 자체를 list로 변환한다.
# 26을 빼는 것 보다 나머지를 구해서 더하는 것이 더 효율적이다. (숫자가 엄청 클 경우)
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

# 다른 사람의 풀이를 보고 파이썬에 대해 새롭게 알게 된 점

# 1. 문자 자체도 부등호가 가능하다.
# if i >= 'A' and i <= 'Z':

# 2. isupper()와 islower() 메서드로 대소문자를 판단할 수 있다.