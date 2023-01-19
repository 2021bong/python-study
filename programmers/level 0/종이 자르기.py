# 종이 자르기

# 첫번째 풀이
# def solution(M, N):
#   if M == 1 and N == 1:
#     return 0
  
#   answer = [M - 1, 0]
#   if M > 1 and N == 1:
#     answer[1] = M - 1
#   elif M == 1 and N > 1:
#     answer[1] = N - 1
#   else:
#     answer[1] = M * (N - 1)
  
#   return sum(answer)

# 다른 사람 풀이 참고
def solution(M, N):
  return M * N - 1
# https://nahwasa.com/entry/%EC%9E%90%EB%B0%94-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A2%85%EC%9D%B4-%EC%9E%90%EB%A5%B4%EA%B8%B0-Lv0-Java
# 알고리즘적 무언가가 있나 했더니 그냥 규칙성을 찾는 것... 이해가 안갔는데 이 링크를 보니 이해가 갔다..
  
# print(solution(2, 2))
# print(solution(2, 5))
# print(solution(1, 1))
# print(solution(1, 9))