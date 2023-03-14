# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    same_count = 0
    zero = 0
    wins = [6,6,5,4,3,2,1]
    for n in lottos:
      if n == 0:
        zero += 1
        continue  
      if n in win_nums:
        same_count += 1
    return [wins[same_count + zero], wins[same_count]]
  
# print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
# print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]	))
# print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

# 다른 사람 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0) # 굳이 반복문을 돌면서 0을 셀 필요없이 한번에 세어줬다.
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]