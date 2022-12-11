# 다음에 올 숫자

def solution(common):
  if len(common) == 2:
    return common[1] + (common[1] - common[0])
  if (common[1] - common[0]) == (common[2] - common[1]):
    return common[len(common) - 1] + (common[1] - common[0])
  else :
    n = common[1] / common[0]
    return int(common[len(common) - 1] * n)
  
  
# print(solution([1, 2, 3, 4]))
# print(solution([2, 4, 8]))

# JS 풀이
# function solution(common) {
#     if (common.length === 2) return common[1] + (common[1] - common[0])
#     if ((common[1] - common[0]) === (common[2] - common[1])) {
#         return common[common.length - 1] + (common[1] - common[0])
#     } else {
#         const n = common[1] / common[0]
#         return common[common.length - 1] * n
#     }
# }