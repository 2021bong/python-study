# 둘만의 암호

def solution(s, skip, index):
    skip = [ord(i) for i in sorted(list(skip))]
    s = [ord(i) for i in s]
    answer = ''
    for str in s:
      rangestr = []
      for i in range(1, index+1):
        newstr = str + i
        while newstr > 122:
          newstr -= 26
        rangestr.append(newstr)
      for s in skip:
        if s in rangestr:
          rangestr.remove(s)
      add = 1
      while len(rangestr) != index:
        if len(rangestr) != 0:
          laststr = rangestr[-1] + add
        else:
          laststr = str + index + add
        if laststr > 122:
          laststr -= 26
        if laststr not in skip:
          add = 1
          rangestr.append(laststr)
        else:
          add += 1
      answer += chr(rangestr[-1])
    
    return answer
    
# print(solution("aukks", "wbqd", 5)) # happy
# print(solution("z", "abcdefghij", 20)) # n
# print(solution("zzzzz", "a", 1)) # bbbbb
# print(solution( "zzzzzz", "abcdefghijklmnopqrstuvwxy", 6)) # zzzzzz
# print(solution( "ybcde", "az", 1)) # bcdef


# 다른 사람 풀이 1
from string import ascii_lowercase # 소문자 알파벳 리스트

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase) # 소문자 알파벳을 집합으로 만든다. s와 skip은 겹치지 않으므로
    a_to_z -= set(skip) # 전체 알파벳 - 스킵할 알파벳 (제외)
    a_to_z = sorted(a_to_z) # 알파벳 정렬 (집합은 순서가 없으므로)
    l = len(a_to_z) # 셀 수 있는 알파벳의 길이

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)} # {알파벳:인덱스} 형태로 딕셔너리를 만든다.

    for i in s: # s를 돌면서
        result += a_to_z[(dic_alpha[i] + index) % l] # 알파벳의 인덱스에 index를 더하고 그 위치의 글자를 더한다.(길이를 초과할 수도 있어서 % 길이를 한다.)

    return result
  
  
# 다른 사람 풀이 2
def solution(s, skip, index):
    alphas = [chr(a) for a in range(ord("a"), ord("z")+1) if chr(a) not in skip] # skip 알파벳이 없는 셀 수 있는 알파벳 리스트를 만들고
    return "".join([alphas[(alphas.index(a) + index) % len(alphas)] for a in s]) # 위와 같이 해당 인덱스로 글자를 찾아 배열은 만든 다음 join
  

# 대부분 다들 셀 수 있는 알파벳만 남겨두고 그 안을 돌면서 셌다. 왜 이 생각을 못했지... 진짜 몇시간을 풀었는데... 나만 바보같이 풀었네.........