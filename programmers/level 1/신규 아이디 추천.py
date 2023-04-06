# 신규 아이디 추천

import re

def solution(new_id):
  answer = []
  for i in new_id:
    upper = re.compile('[A-Z_]')
    upperCheck = upper.match(i)
    if upperCheck != None:
      answer.append(i.lower())
      continue
    sChar = re.compile('[A-Za-z0-9\-_\.]')
    sCharCheck = sChar.match(i)
    if sCharCheck == None:
      continue
    else: 
      answer.append(i)
  answer = ''.join(answer)
  while '..' in answer:
    answer = answer.replace('..','.')
  if answer[0] == '.':
    answer = answer[1:]
    if len(answer) <= 1:
      answer = 'a'
  if answer[-1] == '.':
    answer = answer[0:len(answer)-1]
  if len(answer) == 0:
    answer = 'a'
  if len(answer) >= 16:
    answer = answer[0:15]
    if answer[-1] == '.':
      answer = answer[0:14]
  if len(answer) <= 3:
    answer = answer + answer[-1] * (3 - len(answer))
  return answer

# print(solution('...!@BaT#*..y.abcdefghijklm'))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))



# 다른 사람 풀이 1 -> 이렇게 풀고 싶었는데 정규식을 몰라서...흑흑....
import re

def solution(new_id):
    st = new_id
    st = st.lower() # lower()는 소문자에 해당하는 글자'만' 바꿔준다.
    st = re.sub('[^a-z0-9\-_.]', '', st) # re.sub（정규 표현식, 치환 문자, 대상 문자열）
    st = re.sub('\.+', '.', st) # .여러개를 하나만 있게 변경
    st = re.sub('^[.]|[.]$', '', st) # 시작과 끝 검사
    st = 'a' if len(st) == 0 else st[:15] # 빈문자열일 때 a와 15자로 자르기를 한번에 했다.
    st = re.sub('^[.]|[.]$', '', st) # 자르고 한번 더 검사
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
  

# 다른 사람 풀이 2
from re import sub # 구조분해할당처럼 이렇게 쓸 수도 있다.

def solution(new_id):
    new_id = new_id.lower()
    new_id = sub("[^a-z0-9-_.]", "", new_id)
    new_id = sub("\.+", ".", new_id)
    new_id = sub("(^\.|\.$)", "", new_id)
    new_id = new_id if new_id else "a"
    new_id = sub("\.$", "", new_id[:15])
    new_id = new_id if len(new_id) > 3 else new_id + new_id[-1] * (3 - len(new_id))
    return new_id