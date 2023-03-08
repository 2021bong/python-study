# 실패율

# 22번 케이스 시간 초과
# def solution(N, stages):
#   count_stagess = {}
#   challenger = {}
#   for i in stages:
#     if i in challenger:
#       challenger[i] += 1
#     else:
#       challenger[i] = 1
      
#   for j in range(N):
#     if j + 1 in count_stagess:
#       count_stagess[j + 1] += 1
#     else:
#       count_stagess[j + 1] = 1
      
#   for i in range(1, N+1):
#     if i not in count_stagess:
#       count_stagess[i] = 0
#     if i not in challenger:
#       challenger[i] = 0
      
#   count_stagess = sorted(count_stagess.items(), key=lambda x: x[0])
#   challenger = sorted(challenger.items(), key=lambda x: x[0])
#   answer = {}
#   for f, s in zip(challenger, count_stagess):
#     if s[1] != 0:
#       answer[f[0]] = f[1] / s[1]
#     else:
#       answer[f[0]] = 0
#   if N + 1 in answer:
#     del answer[N + 1]
      
#   return [i[0] for i in sorted(answer.items(), key= lambda x : (-x[1], x[0]))]

# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4,4,4,4,4])) # [4, 1, 2, 3]
# print(solution(5, [4,4,4,4,4])) # [4, 1, 2, 3, 5]
# print(solution(5, [2, 2, 2, 2, 3, 1, 3, 4])) # [4, 3, 2, 1, 5]
  
  
  
# 다른 사람 풀이 1 -> 코드가 간결
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0: # 모든 유저의 스테이지를 확인했는지 파악
            count = stages.count(stage) # 스테이지에 머물러있는 유저의 수
            result[stage] = count / denominator # 실패율 -> 머무른 유저의 수 / 도전한 전체 유저
            denominator -= count # 다음 스테이지 총 도전자 수를 위해 전체에서 앞쪽 스테이지의 수를 빼기
        else:
            result[stage] = 0 # 도전자가 없는 스테이지의 실패율은 0
    return sorted(result, key=lambda x : result[x], reverse=True) # 값이 큰 스테이지대로 정렬
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.15ms, 10MB)
# 테스트 3 〉	통과 (68.69ms, 10.3MB)
# 테스트 4 〉	통과 (393.53ms, 10.9MB)
# 테스트 5 〉	통과 (1417.83ms, 15.1MB)
# 테스트 6 〉	통과 (1.29ms, 9.97MB)
# 테스트 7 〉	통과 (11.50ms, 10MB)
# 테스트 8 〉	통과 (341.63ms, 10.9MB)
# 테스트 9 〉	통과 (1577.58ms, 14.9MB)
# 테스트 10 〉	통과 (204.37ms, 10.9MB)
# 테스트 11 〉	통과 (369.34ms, 10.8MB)
# 테스트 12 〉	통과 (194.34ms, 11.4MB)
# 테스트 13 〉	통과 (419.48ms, 11.3MB)
# 테스트 14 〉	통과 (0.06ms, 10.2MB)
# 테스트 15 〉	통과 (15.01ms, 10.4MB)
# 테스트 16 〉	통과 (10.10ms, 10.3MB)
# 테스트 17 〉	통과 (11.48ms, 10.3MB)
# 테스트 18 〉	통과 (10.52ms, 10.3MB)
# 테스트 19 〉	통과 (2.20ms, 10.1MB)
# 테스트 20 〉	통과 (16.19ms, 10.4MB)
# 테스트 21 〉	통과 (28.65ms, 10.9MB)
# 테스트 22 〉	통과 (1381.26ms, 18MB)
# 테스트 23 〉	통과 (16.55ms, 11.6MB)
# 테스트 24 〉	통과 (58.24ms, 11.5MB)
# 테스트 25 〉	통과 (0.01ms, 10.2MB)
# 테스트 26 〉	통과 (0.01ms, 10.1MB)
# 테스트 27 〉	통과 (0.01ms, 10.4MB)
  
# count함수
# 문자열에 사용 -> 문자열.count(개수를 셀 문자열)
# 'ooyyy'.count('y')

# 리스트에 사용 -> 리스트.count(개수를 셀 요소)
# [1, 1, 1, 2, 3].count(1)
  
  
  
# 다른 사람 풀이 2 -> 위 풀이보다 시간이 적게 듦
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2) # 자리수를 맞추기위한 0 + 최종 스테이지 + 다 깬 유저 의 자리수로 리스트를 만든다.
    for stage in stages: # 스테이지에 머물러 있는 유저를 센다.
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):]) # 슬라이싱을 이용해 앞부터 끝 숫자까지 값을 합함 -> 스테이지 도전자 수 (이 방법 최고다.. 리스트와 슬라이싱을 잘 써야겠다..)
        yet = info[i + 1] # 머물러있는 유저의 수를 info에서 가져옴, 0인덱스는 세지 않으므로 i+1
        if be == 0: # 해당 스테이지에 머무르는 사람이 없으면
            fail.append((str(i + 1), 0)) # 실패율은 0
        else:
            fail.append((str(i + 1), yet / be)) # 머무른 유저의 수 / 스테이지 전체 도전자 수 -> 실패율
    # 반복문이 끝나면 0인덱스는 fail에 추가하지 않았으므로 없음
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0])) # 스테이지 숫자만 반환
    return answer
# 테스트 1 〉	통과 (0.05ms, 10.3MB)
# 테스트 2 〉	통과 (0.09ms, 10.2MB)
# 테스트 3 〉	통과 (1.74ms, 10.6MB)
# 테스트 4 〉	통과 (6.41ms, 10.7MB)
# 테스트 5 〉	통과 (12.70ms, 14.9MB)
# 테스트 6 〉	통과 (0.19ms, 10.3MB)
# 테스트 7 〉	통과 (0.65ms, 10.5MB)
# 테스트 8 〉	통과 (10.90ms, 10.7MB)
# 테스트 9 〉	통과 (20.47ms, 14.8MB)
# 테스트 10 〉	통과 (9.95ms, 10.9MB)
# 테스트 11 〉	통과 (6.55ms, 10.7MB)
# 테스트 12 〉	통과 (17.60ms, 11.3MB)
# 테스트 13 〉	통과 (13.05ms, 11.2MB)
# 테스트 14 〉	통과 (0.06ms, 10.4MB)
# 테스트 15 〉	통과 (7.66ms, 10.5MB)
# 테스트 16 〉	통과 (3.70ms, 10.4MB)
# 테스트 17 〉	통과 (4.33ms, 10.7MB)
# 테스트 18 〉	통과 (2.35ms, 10.2MB)
# 테스트 19 〉	통과 (0.82ms, 10.4MB)
# 테스트 20 〉	통과 (3.23ms, 10.4MB)
# 테스트 21 〉	통과 (10.97ms, 10.7MB)
# 테스트 22 〉	통과 (13.44ms, 17.9MB)
# 테스트 23 〉	통과 (15.48ms, 11.6MB)
# 테스트 24 〉	통과 (18.68ms, 11.7MB)
# 테스트 25 〉	통과 (0.03ms, 10.3MB)
# 테스트 26 〉	통과 (0.03ms, 10.3MB)
# 테스트 27 〉	통과 (0.02ms, 10.4MB)