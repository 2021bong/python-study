# 두 개 뽑아서 더하기

def solution(numbers):
  answer = []
  for i in range(len(numbers)):
    j = i + 1
    while j < len(numbers):
      answer.append(numbers[i] + numbers[j])
      j += 1
  return sorted(list(set(answer)))

# print(solution([2,1,3,4,1]))
# print(solution([5,0,2,7]))