# 문자열 내 마음대로 정렬하기

def solution(strings, n):
  answer = sorted(strings, key = lambda x : (x[n], x))
  return answer

# print(solution(["sun", "bed", "car"], 1))
# print(solution(["abce", "abcd", "cdx"], 2))