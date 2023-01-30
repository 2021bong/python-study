# 외계어 사전

def solution(spell, dic):
  contain = 0
  for alien_word in dic:
    for char in spell:
      if char in alien_word:
        contain += 1
      if contain == len(spell):
        return 1
    contain = 0
  return 2
  
  
# 다른 사람의 풀이 
# 1. 집합의 특성을 활용
# spell ['d','z','x'], dic ['dzxx']의 경우에 대한 의견이 있었음
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2

# 2. 문자열을 정렬해서 비교
def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2
  
# print(solution(["p", "o", "s"],["sod", "eocd", "qixm", "adio", "soo"]))
# print(solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"]))
# print(solution(["s", "o", "m", "d"],["moos", "dzx", "smm", "sunmmo", "som"]	))