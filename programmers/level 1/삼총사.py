# 삼총사

def solution(number):
  count = 0
  for i in range(0, len(number)-2): # 다른 사람의 풀이를 보고 1,2번째 for문에 전체 길이를 2와 1씩 빼줬다. 그랬더니 1(0.11ms), 6(0.09ms), 8(0.11ms), 12(0.08ms) 케이스 소요시간이 0.05ms 아래로 줄었다.
    for j in range(i+1, len(number)-1):
      for k in range(j+1, len(number)):
        if (number[i] + number[j] + number[k]) == 0:
          count += 1
    
  return count

# print(solution([-2, 3, 0, 2, -5]))
# print(solution([-3, -2, -1, 0, 1, 2, 3]))
# print(solution([-1, 1, -1, 1]))

# 다른 사람 풀이
# 모듈을 사용해 간단하게 풀이
# from itertools import combinations
def solution (number) :
    from itertools import combinations # import를 함수 안에서 할 수도 있는 것 같다.
    cnt = 0
    for i in combinations(number,3) : # combinations(iterable, r) : iterable에서 원소 개수가 r개인 조합 뽑기
        if sum(i) == 0 :
            cnt += 1
    return cnt