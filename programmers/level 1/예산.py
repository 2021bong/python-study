# 예산

def solution(d, budget):
    d = sorted(d)
    count = 0
    for m in d:
      budget = budget - m
      if budget < 0:
        return count
      count += 1
    return count
  
# print(solution([1,3,2,5,4],9)) # 3
# print(solution([2,2,3,3], 10)) # 4

# sort() vs sorted()
# list.sort() -> 리스트 원본값 수정
# sorted(list) -> 원본 값은 그대로이며 정렬 값을 반환