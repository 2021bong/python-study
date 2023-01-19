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
  
print(solution(2, 2))
print(solution(2, 5))
print(solution(1, 1))
print(solution(1, 9))