# 폰켓몬

def solution(nums):
    max_count = len(nums) // 2
    sort_of_mons = len(set(nums))
    if max_count < sort_of_mons:
      return max_count
    else:
      return sort_of_mons
  
print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))

# 다른 사람 풀이
# min 함수를 사용했다.
def solution(ls):
    return min(len(ls)/2, len(set(ls))) # set에도 len메서드가 있어서 list로 굳이 만들 필요가 없다.