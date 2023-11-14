# 다른 사람 풀이
# bfs 풀이
from collections import deque
def solution(maps):
    max = len(maps) #maps 배열의 행 - y
    may = len(maps[0]) # maps 배열의 열 - x
    check = [[0]*may for i in range(max)] # 방문 여부 체크를 위한 배열
    # check에다가는 그냥 순서만 표시 (순서 == 방문여부)
    # 방문 가능성 (=벽인지 아닌지)는 maps에서 처리
    dy,dx = [-1,0,1,0],[0,1,0,-1] # 상우하좌
    q = deque([(0,0)]) # deque에 시작점 넣음
    check[0][0] = 1 # 시작점 방문 체크(1)

    while q:
        y,x = q.popleft() # 첫번째 요소 꺼냄
        for i in range(4): # 상하좌우 이동가능 체크
            ny,nx = y+dy[i] ,x+dx[i] # 상하좌우 이동된 좌표 ny, nx를
            if 0<=ny<max and 0<=nx<may: # 이동가능 범위를 벗어나는지 체크
                if check[ny][nx] == 0 and maps[ny][nx] == 1: # 아직 방문하지 않았고 and map에서 이동이 가능하면
                    check[ny][nx] = check[y][x] + 1 # 원래 있던 좌표에 1을 더한 값을 이동한 좌표에 체크(순서? == 이동한 거리?)
                    q.append((ny,nx)) # 또 이동해야하므로 새로운 좌표를 q에 추가
    if check[max-1][may-1] == 0: # 방문하지 못했다면
        return -1
    else:
        return check[max-1][may-1] # 이동할 때 마다 순서를 체크했으므로 목표 지점까지 도달했을때 순서 == 이동거리를 반환



# bfs 찾아보고 다시 풀기
def solution(maps):
  max_y = len(maps)
  max_x = len(maps[0])
  check = [[0]*max_x for i in range(max_y)]
  move = [(-1, 0),(1, 0),(0, -1),(0, 1)] # 상하좌우 (y, x)
  q = []
  check[0][0] = 1
  q.append((0, 0))
  while q:
    y, x = q.pop(0);
    for m_y, m_x in move:
      n_x = x + m_x
      n_y = y + m_y
      if 0 <= n_x and n_x < max_x and 0 <= n_y and n_y < max_y:
        if maps[n_y][n_x] != 0 and check[n_y][n_x] == 0:
          check[n_y][n_x] = check[y][x] + 1
          q.append((n_y, n_x))
  if check[max_y-1][max_x-1] < 1:
    return -1

  return check[max_y-1][max_x-1]
# pop(0)안하고 pop()해서 계속 틀려서 고뇌함
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.1MB)
# 테스트 3 〉	통과 (0.04ms, 10.1MB)
# 테스트 4 〉	통과 (0.03ms, 10.1MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.05ms, 10.2MB)
# 테스트 7 〉	통과 (0.06ms, 10.3MB)
# 테스트 8 〉	통과 (0.04ms, 10.3MB)
# 테스트 9 〉	통과 (0.05ms, 10.3MB)
# 테스트 10 〉	통과 (0.05ms, 10.1MB)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.4MB)
# 테스트 13 〉	통과 (0.07ms, 10.2MB)
# 테스트 14 〉	통과 (0.06ms, 10.2MB)
# 테스트 15 〉	통과 (0.04ms, 10.2MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.05ms, 10.4MB)
# 테스트 18 〉	통과 (0.01ms, 10.1MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
# 테스트 21 〉	통과 (0.01ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (10.68ms, 10.3MB)
# 테스트 2 〉	통과 (3.06ms, 10.2MB)
# 테스트 3 〉	통과 (7.49ms, 10.3MB)
# 테스트 4 〉	통과 (4.63ms, 10.3MB)

from collections import deque
def solution(maps):
  max_y = len(maps)
  max_x = len(maps[0])
  check = [[0]*max_x for i in range(max_y)]
  move = [(-1, 0),(1, 0),(0, -1),(0, 1)] # 상하좌우 (y, x)
  q = deque([])
  check[0][0] = 1
  q.append((0, 0))
  while q:
    y, x = q.popleft();
    for m_y, m_x in move:
      n_x = x + m_x
      n_y = y + m_y
      if 0 <= n_x and n_x < max_x and 0 <= n_y and n_y < max_y:
        if maps[n_y][n_x] != 0 and check[n_y][n_x] == 0:
          check[n_y][n_x] = check[y][x] + 1
          q.append((n_y, n_x))
  if check[max_y-1][max_x-1] < 1:
    return -1

  return check[max_y-1][max_x-1]
# popleft() 보고 첫번째 요소!하고 번뜩 생각남
# 범위 벗어났는지, 벽인지, 방문했는지 조건을 나눴을 때 시간이 더 적게 걸림
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.05ms, 10.2MB)
# 테스트 6 〉	통과 (0.04ms, 10.3MB)
# 테스트 7 〉	통과 (0.06ms, 10.4MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.09ms, 10.3MB)
# 테스트 10 〉	통과 (0.05ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.1MB)
# 테스트 12 〉	통과 (0.04ms, 10.2MB)
# 테스트 13 〉	통과 (0.09ms, 10.3MB)
# 테스트 14 〉	통과 (0.03ms, 10.2MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.05ms, 10.2MB)
# 테스트 18 〉	통과 (0.02ms, 10.2MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (10.31ms, 10.3MB)
# 테스트 2 〉	통과 (2.86ms, 10.3MB)
# 테스트 3 〉	통과 (6.55ms, 10.3MB)
# 테스트 4 〉	통과 (4.86ms, 10.3MB)

# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1
# print(solution([[1, 1, 0], [1, 0, 0], [1, 1, 1]])) # 5
# print(solution([
# [1, 0, 1, 1, 1],
# [1, 0, 1, 0, 1],
# [1, 0, 1, 1, 1],
# [1, 1, 1, 0, 0],
# [0, 0, 0, 1, 1],
# ]))
# print(solution([[1],[1]])) # 2
