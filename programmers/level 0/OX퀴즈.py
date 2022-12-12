# OX 퀴즈

# 파이썬 split
# str.split()
# str.split('구분자')
# str.split('구분자', 분할횟수)
# str.split(sep='구분자', maxsplit=분할횟수)

# 다른 사람의 풀이
# eval이 뭐야..

def solution(quiz):
  splitQuiz = []
  for i in quiz:
    splitQuiz.append(i.split(' '))
  
  for i, value in enumerate(splitQuiz):
    first, oper, second, equal, ans = value
    if oper == '+':  
      if int(first) + int(second) == int(ans):
        quiz[i] = "O"
      else :
        quiz[i] = "X"
    else :
      if int(first) - int(second) == int(ans):
        quiz[i] = "O"
      else :
        quiz[i] = "X"
      
  return quiz

# print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
# print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))