# 특이한 정렬

# sorted(iterable, /, *, key=None, reverse=False)
# key 는 하나의 인자를 받는 함수를 지정하는데, iterable의 각 요소들로부터 비교 키를 추출하는 데 사용됩니다 (예를 들어, key = str.lower). 기본값은 None 입니다 (요소를 직접 비교합니다).
# reverse 는 논리값입니다. True 로 설정되면, 각 비교가 뒤집힌 것처럼 리스트 요소들이 정렬됩니다.

# 첫 번째 인자를 기준으로 오름차순 정렬을 먼저 한다.
# 그 결과를 가지고 두 번째 인자를 기준으로 내림차순 정렬(-를 붙이면 내림차순 정렬)

def solution(numlist, n):
  numlist = sorted(numlist, key = lambda x: (abs(n - x), -x))
  return numlist

print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))