# 같은 숫자는 싫어

def solution(arr):
  answer = []
  for n in arr:
    if len(answer) == 0:
      answer.append(n)
    elif n != answer[-1]:
      answer.append(n)
  return answer

# 다른 사람의 풀이
# [:] 슬라이싱을 사용해서 a배열의 마지막 원소를 가져옴
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
  
a = []
print(a[-1:]) # []
# print(a[-1]) # 에러 IndexError:list index out of range