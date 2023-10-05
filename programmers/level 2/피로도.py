from itertools import permutations # 진짜 최고다.... 순열을 알아서 만들어준다...

def solution(k, dungeons): # [최소피로도, 소모피로도]
    all_d = []
    for i in permutations(dungeons,len(dungeons)):
        all_d.append(list(i))
    d_count = []
    for r in all_d:
      copy_k = k
      count = 0
      for hp in r:
        min_hp, use_hp = hp[0], hp[1]
        if copy_k >= min_hp:
          copy_k -= use_hp
          count += 1
      d_count.append(count)  
    return max(d_count)
# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.17ms, 10.2MB)
# 테스트 4 〉	통과 (0.19ms, 10.2MB)
# 테스트 5 〉	통과 (0.74ms, 10.4MB)
# 테스트 6 〉	통과 (5.36ms, 10.4MB)
# 테스트 7 〉	통과 (50.15ms, 15.7MB)
# 테스트 8 〉	통과 (56.96ms, 15.7MB)
# 테스트 9 〉	통과 (0.10ms, 10.2MB)
# 테스트 10 〉	통과 (5.30ms, 10.5MB)
# 테스트 11 〉	통과 (0.02ms, 10.1MB)
# 테스트 12 〉	통과 (49.46ms, 15.7MB)
# 테스트 13 〉	통과 (51.99ms, 15.5MB)
# 테스트 14 〉	통과 (44.40ms, 15.6MB)
# 테스트 15 〉	통과 (46.95ms, 15.8MB)
# 테스트 16 〉	통과 (6.01ms, 10.5MB)
# 테스트 17 〉	통과 (46.97ms, 15.6MB)
# 테스트 18 〉	통과 (0.04ms, 10.2MB)
# 테스트 19 〉	통과 (0.18ms, 10.2MB)

# print(solution(80, [[80,20],[50,40],[30,10]])) # 3
# print(solution(8, [[7, 3], [5, 4], [1, 1]])) # 3
# print(solution(10, [[9, 2], [10, 3], [7, 3], [5, 4], [1, 1]])) # 4


# 다른 사람 풀이 1 - 풀이 이해못함
# 백트래킹 -> 나중에 찾아볼 것 
# global <변수이름>와 같이 global 키워드를 사용하면 전역변수인 <변수이름>을 사용하겠다는 의미이다.
answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer # 전역변수 answer 사용
    if cnt > answer: # 가장 큰 cnt를 갱신
        answer = cnt

    for j in range(N): # 던전의 길이만큼 반복
        if k >= dungeons[j][0] and not visited[j]: # 던전 j의 최소피로도가 남은 체력보다 작거나 같으면서, j던전의 탐험횟수가 0일때
            visited[j] = 1 # 1로 바꿔주고
            # 재귀
            dfs(k - dungeons[j][1], cnt + 1, dungeons) # (남은 체력 - 던전j 소모피로도, 증가된 cnt, 던전)
            visited[j] = 0
            # visited를 1로 바꾸고 재귀를 실행하고 0으로 다시 초기화


def solution(k, dungeons):
    global N, visited # 전역변수 N, visited 사용
    N = len(dungeons)
    visited = [0] * N # 던전의 길이만큼 탐험가능 횟수를 셀수있도록 배열 생성
    dfs(k, 0, dungeons)
    return answer
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.27ms, 10.2MB)
# 테스트 5 〉	통과 (1.02ms, 10.1MB)
# 테스트 6 〉	통과 (2.96ms, 10.3MB)
# 테스트 7 〉	통과 (18.35ms, 10.3MB)
# 테스트 8 〉	통과 (47.82ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.1MB)
# 테스트 10 〉	통과 (0.93ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (2.28ms, 10.2MB)
# 테스트 13 〉	통과 (0.26ms, 10.2MB)
# 테스트 14 〉	통과 (0.09ms, 10.3MB)
# 테스트 15 〉	통과 (0.04ms, 10.4MB)
# 테스트 16 〉	통과 (0.04ms, 10.3MB)
# 테스트 17 〉	통과 (0.10ms, 10.2MB)
# 테스트 18 〉	통과 (0.02ms, 10.2MB)
# 테스트 19 〉	통과 (0.10ms, 10.2MB)


# 다른 사람 풀이 2
# 테스트케이스 18, 19를 통과하지는 못했지만 던전 효율성을 계산한게 인상적 -> 냅색 알고리즘을 찾아보라는 의견이 있다..
def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0],x[1])) # (최소필요 피로도 + 소모피로도) / 최소필요 피로도, 소모피로도 순으로 정렬 -> 던전 효율성을 계산하여 정렬
    print(dungeons)
    for x,y in dungeons:
        print("x :", x, "y : ", y)
        if k >= x: # 남은 체력이 최소필요 피로도보다 같거나 많을 때
            k -= y # 남은 체력에서 소모필요도를 빼고
            answer += 1 # 탐험횟수를 올림
    return answer
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.4MB)
# 테스트 10 〉	통과 (0.02ms, 10.4MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10.4MB)
# 테스트 14 〉	통과 (0.02ms, 10.3MB)
# 테스트 15 〉	통과 (0.02ms, 10.1MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.02ms, 10.2MB)
# 테스트 18 〉	실패 (0.01ms, 10.3MB)
# 테스트 19 〉	실패 (0.01ms, 10.3MB)
print(solution(80, [[80,20],[50,40],[30,10]])) # 3