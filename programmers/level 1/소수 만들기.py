# 소수 만들기

import math
from itertools import combinations

def solution(nums):
    max_total = sum(sorted(nums, reverse=True)[:3:])
    prime_arr = [True] * max_total
    prime_arr[0] = False
    for i in range(2, int(math.sqrt(max_total)+1)):
      j = 2
      while (i * j) <= max_total:
        prime_arr[(i * j)-1] = False
        j += 1
    prime_arr = [i + 1 for i in range(len(prime_arr)) if prime_arr[i] == True]
    comb = list(combinations(nums, 3))
    sums = [sum(comb[i]) for i in range(len(comb))]
    answer = []
    for i in range(len(sums)):
      if sums[i] in prime_arr:
        answer.append(sums[i])
    return len(answer)
# 테스트 1 〉	통과 (1.60ms, 10.4MB)
# 테스트 2 〉	통과 (2.12ms, 10.5MB)
# 테스트 3 〉	통과 (0.64ms, 10.2MB)
# 테스트 4 〉	통과 (0.32ms, 10.3MB)
# 테스트 5 〉	통과 (3.71ms, 10.5MB)
# 테스트 6 〉	통과 (10.82ms, 10.7MB)
# 테스트 7 〉	통과 (1.38ms, 10.2MB)
# 테스트 8 〉	통과 (23.04ms, 11.6MB)
# 테스트 9 〉	통과 (3.03ms, 10.3MB)
# 테스트 10 〉	통과 (24.62ms, 11.6MB)
# 테스트 11 〉	통과 (0.11ms, 10.1MB)
# 테스트 12 〉	통과 (0.10ms, 10.1MB)
# 테스트 13 〉	통과 (0.18ms, 10MB)
# 테스트 14 〉	통과 (0.06ms, 10.3MB)
# 테스트 15 〉	통과 (0.05ms, 10.4MB)
# 테스트 16 〉	통과 (111.96ms, 11.6MB)
# 테스트 17 〉	통과 (85.97ms, 11.8MB)
# 테스트 18 〉	통과 (1.59ms, 10.2MB)
# 테스트 19 〉	통과 (1.32ms, 10.2MB)
# 테스트 20 〉	통과 (83.41ms, 12MB)
# 테스트 21 〉	통과 (94.14ms, 11.9MB)
# 테스트 22 〉	통과 (15.57ms, 10.4MB)
# 테스트 23 〉	통과 (0.01ms, 10.1MB)
# 테스트 24 〉	통과 (62.44ms, 11.7MB)
# 테스트 25 〉	통과 (61.20ms, 11.7MB)
# 테스트 26 〉	통과 (0.01ms, 10.2MB)
  
# print(solution([1,2,3,4]))
# print(solution([1,2,7,6,4]))

# 다른 사람 풀이 1
# 굳이 에라토스테네스의 체를 만들지 않고 combinations를 사용해 합들을 만들어내고 거기에 합보다 작은 i를 나눠가며 나누어 떨어지면 for문을 종료하고 아니면 카운트를 하나 올린다.
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
  
# 다른 사람 풀이 2
# 시간이 얼마 안걸린다...!
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1): # 굳이 math.sqrt를 사용하지않고 0.5제곱을 해서 제곱근을 구하는 방법도 있다.
        if num % i == 0: # 제한 사항에 중복된 숫자가 들어있지 않다고 했으므로 최소 [1,2,3]의 합 6이상이므로 2부터 약 합의 반절까지 반복문을 돌렸을 때 i에 나누어떨어지면 소수가 아니다.
            return False
    return True
def solution(nums):
    from itertools import combinations
    comb = list(combinations(nums, 3))
    cnt = 0
    for tup in comb:
        if is_prime(sum(tup)):
            cnt += 1
    return cnt
# 테스트 1 〉	통과 (2.24ms, 10.3MB)
# 테스트 2 〉	통과 (3.00ms, 10.3MB)
# 테스트 3 〉	통과 (0.58ms, 10.3MB)
# 테스트 4 〉	통과 (0.50ms, 10.1MB)
# 테스트 5 〉	통과 (5.94ms, 10.3MB)
# 테스트 6 〉	통과 (5.12ms, 10.6MB)
# 테스트 7 〉	통과 (0.32ms, 10.2MB)
# 테스트 8 〉	통과 (12.02ms, 10.9MB)
# 테스트 9 〉	통과 (1.14ms, 10.3MB)
# 테스트 10 〉	통과 (11.03ms, 10.8MB)
# 테스트 11 〉	통과 (0.10ms, 10.2MB)
# 테스트 12 〉	통과 (0.06ms, 10.3MB)
# 테스트 13 〉	통과 (0.13ms, 10.1MB)
# 테스트 14 〉	통과 (0.09ms, 10.4MB)
# 테스트 15 〉	통과 (0.08ms, 10.3MB)
# 테스트 16 〉	통과 (25.08ms, 11MB)
# 테스트 17 〉	통과 (12.36ms, 11.1MB)
# 테스트 18 〉	통과 (0.18ms, 10.3MB)
# 테스트 19 〉	통과 (0.02ms, 10.2MB)
# 테스트 20 〉	통과 (21.33ms, 11.3MB)
# 테스트 21 〉	통과 (22.76ms, 11.2MB)
# 테스트 22 〉	통과 (2.27ms, 10.3MB)
# 테스트 23 〉	통과 (0.02ms, 10.3MB)
# 테스트 24 〉	통과 (15.68ms, 11.2MB)
# 테스트 25 〉	통과 (17.95ms, 11.1MB)
# 테스트 26 〉	통과 (0.03ms, 10.1MB)

# 굳이 에라토스테네스의 체를 만들지않고 바로 합의 반절까지만 비교해서 카운트를 올려도 충분했을 것 같다.