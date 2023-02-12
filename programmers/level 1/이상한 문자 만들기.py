# 이상한 문자 만들기

def solution(s):
    answer = []
    for word in s.split(' '):
      word = list(word)
      for i in range(len(word)):
        if i % 2 == 0:
          word[i] = word[i].upper()
        else:
          word[i] = word[i].lower()
      answer.append(''.join(word))
    return ' '.join(answer)
  
# print(solution('try hello world'))