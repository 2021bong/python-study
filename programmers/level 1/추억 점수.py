# 추억 점수

def solution(name, yearning, photo):
    scores = {}
    for n, y in zip(name, yearning):
      scores[n] = y
    answer = []
    for ph in photo:
      s = 0
      for p in ph:
        if p in scores:
          s += scores[p]
      answer.append(s)
    return answer
  
# print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
# print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
# print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]))