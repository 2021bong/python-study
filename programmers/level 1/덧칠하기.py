# 덧칠하기

# 양 끝이 멀어서 겹치는 곳이 안생길때 어떻게 해야할지 모르겠음... 최대점수 54/100...
def solution(n, m, section):
    if m == 1:
      return section[-1] - section[0] + 1
    count = 0
    for n in range(section[0], section[-1]+1, m - 1):
      count += 1
    return count
  
# print(solution(8, 4, [2,3,6]))
# print(solution(5, 4, [1,3]))
# print(solution(4, 1, [1,2,3,4]))
# print(solution(8, 2, [2, 6])) # 2


# 다른 사람 풀이 1
def solution(n, m, section):
    paint, answer = section[0]-1, 0 # 칠해야하는 가장 첫번째 - 1(이렇게 해야 m만큼 칠해진 구역 중 가장 큰 숫자의 구역 번호가 나옴), 횟수
    for v in section:
        if paint < v: # 칠해야하는 구역 번호가 칠을 시작할 수 있는 구역의 번호보다 큰지 확인
            paint = v+m-1 # 칠해야하는 구역부터 m만큼 칠했으니 다음에 칠하기 시작하는 칸 계산
            answer += 1 # 칠한 횟수 + 1

    return answer
# 칠해야하는 구역 번호가 칠해져있는지를 검토해가면서 횟수를 카운트한다고 보면 될 것 같다.
  
  
# 다른 사람 풀이 2 -> deque 사용
from collections import deque
def solution(n, m, section):
    answer = 0
    section = deque(section) # section을 deque에 넣는다.
    while section: # 0. deque에 요소가 있을 때 (deque에 요소가 없을 때까지 반복)
        start = section.popleft() # 1. 가장 빠른 구역 번호. deque에서 꺼낸다.
        while section: # 2. deque에 요소가 있을 때
            if section[0] >= start + m: # 3-1. 남아 있는 가장 빠른 deque요소가 (가장빠른 구역 번호 + m)보다 크거나 같으면 빠져나온다. (서로 겹치지 않는 먼 번호)
                break
            section.popleft() # 3-2. deque 요소를 꺼낸다.
        answer += 1 # 4. 칠한 횟수를 센다.
    return answer


# 다른 사람 풀이 3 -> 1번과 유사한 풀이
def solution(n, m, section):
    answer = 1
    prev = section[0] # 가장 빠른 구역번호
    for sec in section: # section을 돌면서
        if sec - prev >= m: # 구역을 돌면서 가장 빠른 구역 번호를 뺏을 때 m보다 크거나 같으면
            prev = sec # 가장 빠른 구역번호를 현재 구역 번호로 바꿔준다.
            answer += 1 # 그리고 칠한 횟수를 올려준다.

    return answer
  

# 다른 사람 풀이 4
def solution(n, m, section):
    answer = 0
    section = set(section) # 이 코드를 빼면 12, 17, 35 시간초과가 뜬다. 왜..? 아마도 set자료형 탐색 시간이 O(1)라서 그런듯..

    loc = 1 # 다짜고짜 1부터 돈다.
    while loc <= n: # 총 벽의 길이보다 작을 때까지
        if loc in section: # section에 loc이 있으면
            loc += m # loc만큼 m을 더해서 칠한 구역을 제외하고 칠하기 시작할 구역 번호로 이동
            answer += 1 # 칠한 횟수 카운트
        else:
            loc += 1 # section에 없다면 숫자를 1 올린다.

    return answer