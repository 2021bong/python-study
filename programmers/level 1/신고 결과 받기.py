def solution(id_list, report, k):
    # report "이용자id 신고한id"
    user_report_count = {}
    user_report = {}
    for user in id_list:
      user_report_count[user] = 0
      user_report[user] = []
    for r in report:
      from_user, to_user = r.split()
      if to_user not in user_report[from_user]:
        user_report_count[to_user] += 1
        user_report[from_user].append(to_user)
    block_user = []
    for name, count in user_report_count.items():
      if count >= k and name not in block_user:
        block_user.append(name)
    answer = []
    for user, report_data in user_report.items():
      cnt = 0
      for name in report_data:
        if name in block_user:
          cnt += 1
      answer.append(cnt)
    return answer
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (1763.82ms, 37.9MB)
# 테스트 4 〉	통과 (0.04ms, 10.1MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (1.39ms, 10.4MB)
# 테스트 7 〉	통과 (6.37ms, 10.8MB)
# 테스트 8 〉	통과 (9.27ms, 10.9MB)
# 테스트 9 〉	통과 (478.74ms, 23.1MB)
# 테스트 10 〉	통과 (365.16ms, 23MB)
# 테스트 11 〉	통과 (1561.28ms, 37.7MB)
# 테스트 12 〉	통과 (0.61ms, 10.2MB)
# 테스트 13 〉	통과 (0.41ms, 10.4MB)
# 테스트 14 〉	통과 (552.40ms, 22.1MB)
# 테스트 15 〉	통과 (433.39ms, 31MB)
# 테스트 16 〉	통과 (0.31ms, 10.2MB)
# 테스트 17 〉	통과 (0.27ms, 10.3MB)
# 테스트 18 〉	통과 (1.00ms, 10.3MB)
# 테스트 19 〉	통과 (2.51ms, 10.3MB)
# 테스트 20 〉	통과 (536.95ms, 22MB)
# 테스트 21 〉	통과 (853.21ms, 30.9MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.1MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)

# set 이용해서 다시 풀기
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    user_report_count = {}
    report = set(report)
    for user in id_list:
      user_report_count[user] = 0
    for r in report:
      from_user, to_user = r.split()
      user_report_count[to_user] += 1
    for r in report:
      from_user, to_user = r.split()
      if user_report_count[to_user] >= k:
        answer[id_list.index(from_user)] += 1
    return answer
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (1354.40ms, 39.3MB)
# 테스트 4 〉	통과 (0.04ms, 10.3MB)
# 테스트 5 〉	통과 (0.04ms, 10.2MB)
# 테스트 6 〉	통과 (1.03ms, 10.4MB)
# 테스트 7 〉	통과 (1.87ms, 10.6MB)
# 테스트 8 〉	통과 (2.71ms, 10.9MB)
# 테스트 9 〉	통과 (355.22ms, 23.9MB)
# 테스트 10 〉	통과 (63.57ms, 23.8MB)
# 테스트 11 〉	통과 (519.98ms, 39.4MB)
# 테스트 12 〉	통과 (0.52ms, 10.4MB)
# 테스트 13 〉	통과 (0.23ms, 10.2MB)
# 테스트 14 〉	통과 (416.18ms, 20.1MB)
# 테스트 15 〉	통과 (92.81ms, 31.4MB)
# 테스트 16 〉	통과 (0.19ms, 10.4MB)
# 테스트 17 〉	통과 (0.24ms, 10.3MB)
# 테스트 18 〉	통과 (0.85ms, 10.4MB)
# 테스트 19 〉	통과 (1.35ms, 10.4MB)
# 테스트 20 〉	통과 (370.73ms, 20MB)
# 테스트 21 〉	통과 (711.04ms, 31.3MB)
# 테스트 22 〉	통과 (0.01ms, 10.3MB)
# 테스트 23 〉	통과 (0.01ms, 10.3MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)
  
# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

# 다른 사람 풀이 1
def solution(id_list, report, k):
    answer = [0] * len(id_list) # 메일 받는 횟수를 0으로 배열 생성
    reports = {x : 0 for x in id_list} # 유저이름을 key로 신고 당한 횟수 카운트 할 객체 생성

    for r in set(report): # 어차피 한 사람이 여러번 신고해도 1번만 적용되므로 set으로 중복을 없앤다.
        reports[r.split()[1]] += 1 # 신고당한 사람 숫자를 올린다.

    for r in set(report):
        if reports[r.split()[1]] >= k: # 신고당한 숫자가 k보다 많은 사람은
            answer[id_list.index(r.split()[0])] += 1 # answer과 id_list의 인덱스는 같으므로 정지먹은 사람의 갯수를 올린다.

    return answer
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.05ms, 10.2MB)
# 테스트 3 〉	통과 (1304.84ms, 39.7MB)
# 테스트 4 〉	통과 (0.04ms, 10.3MB)
# 테스트 5 〉	통과 (0.04ms, 10.4MB)
# 테스트 6 〉	통과 (1.22ms, 10.5MB)
# 테스트 7 〉	통과 (2.21ms, 10.6MB)
# 테스트 8 〉	통과 (3.53ms, 10.8MB)
# 테스트 9 〉	통과 (377.28ms, 24.1MB)
# 테스트 10 〉	통과 (71.87ms, 23.9MB)
# 테스트 11 〉	통과 (577.75ms, 39.6MB)
# 테스트 12 〉	통과 (0.62ms, 10.3MB)
# 테스트 13 〉	통과 (0.24ms, 10.2MB)
# 테스트 14 〉	통과 (440.28ms, 20.3MB)
# 테스트 15 〉	통과 (104.12ms, 31.6MB)
# 테스트 16 〉	통과 (0.24ms, 10.2MB)
# 테스트 17 〉	통과 (0.24ms, 10.3MB)
# 테스트 18 〉	통과 (0.88ms, 10.4MB)
# 테스트 19 〉	통과 (1.52ms, 10.3MB)
# 테스트 20 〉	통과 (420.10ms, 20.3MB)
# 테스트 21 〉	통과 (739.83ms, 31.5MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.1MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)


# 다른 사람 풀이 2
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list} # 해당 유저를 신고한 ID
    for i in set(report): # set으로 중복을 없앤다.
        i = i.split()
        dic_report[i[1]].append(i[0]) # 신고당한사람(key):[신고한사람]을 넣는다.

    for key, value in dic_report.items():
        if len(value) >= k: # len(value) == 신고 받은 횟수
            for j in value:
                answer[id_list.index(j)] += 1 # id_list에서 이름으로 인덱스를 찾아 그 사람이 메일 받을 횟수를 올린다.

    return answer
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (1391.13ms, 46.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.96ms, 10.4MB)
# 테스트 7 〉	통과 (1.46ms, 10.6MB)
# 테스트 8 〉	통과 (2.41ms, 11MB)
# 테스트 9 〉	통과 (370.20ms, 27MB)
# 테스트 10 〉	통과 (50.42ms, 26.9MB)
# 테스트 11 〉	통과 (736.91ms, 46.4MB)
# 테스트 12 〉	통과 (0.53ms, 10.2MB)
# 테스트 13 〉	통과 (0.19ms, 10.2MB)
# 테스트 14 〉	통과 (423.51ms, 24.1MB)
# 테스트 15 〉	통과 (82.00ms, 36.7MB)
# 테스트 16 〉	통과 (0.17ms, 10.3MB)
# 테스트 17 〉	통과 (0.25ms, 10.3MB)
# 테스트 18 〉	통과 (0.78ms, 10.5MB)
# 테스트 19 〉	통과 (2.13ms, 10.3MB)
# 테스트 20 〉	통과 (383.22ms, 24.1MB)
# 테스트 21 〉	통과 (725.99ms, 36.7MB)
# 테스트 22 〉	통과 (0.01ms, 10.4MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)