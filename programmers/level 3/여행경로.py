from collections import deque
def solution(tickets):
    tickets = sorted(tickets, key=lambda x : x[1])
    route = ['ICN']
    firstICN = 0
    for i, name in enumerate(tickets):
      if name[0] == 'ICN':
        firstICN = i
        break
    used = [False]*len(tickets)
    used[firstICN] = True
    q = deque([tickets[firstICN]])
    while q:
      start, arrive = q.popleft()
      for i, t in enumerate(tickets):
        t_s, t_a = t[0], t[1]
        if arrive == t_s and not used[i]:
          route.append(t_s)
          q.append(t)
          if int(used.count(False)) == 1:
            route.append(t_a)
          used[i] = True
          break;
    return route
# 미리 정렬하고 시작하면 아래 세번째를 통과를 못함..
# 풀 수 있을 줄 알았는데 안됨.. 레벨 3문제라 dfs/bfs 박살내고 다시 돌아오는걸로..
# tip 1
# "모든 티켓을 사용하여야 한다.", "사전 상으로 빠른 곳을 먼저 방문한다." 라는 제한 사항이 있습니다.
# 위의 INPUT의 경우 2번째 규칙에 의해 A를 먼저 방문하여야 할 것 같지만 그렇게 되면 A를 출발지로 하는 티켓이 없어 방문하고자 하는 나라를 
# 모두 방문할 수 없는 예외 케이스가 생깁니다. 그렇기 때문에 B를 먼저 방문해야 합니다. 이 경우의 예외처리를 잘 해주시면 1, 2번도 맞을 수 있습니다.
# tip 2
# 1,2,3의 모든 조건을 엄격하게 지킬 것
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
# 테스트 1 〉	실패 (0.03ms, 10.4MB)
# 테스트 2 〉	실패 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]])) # ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]