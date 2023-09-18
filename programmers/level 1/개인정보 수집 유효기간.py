def solution(today, terms, privacies):
    from datetime import date
    y, m, d = today.split('.')
    today = date(int(y), int(m), int(d))
    s_terms = {}
    for t in terms:
      term_id, term_month = t.split(' ')
      s_terms[term_id] = int(term_month)
  
    answer = []
    for i, u in enumerate(privacies):
      u_date, term = u.split(' ')
      u_year, u_month, u_day = u_date.split('.')
      add_year =  s_terms[term] / 12
      c_month = s_terms[term] % 12
      rest_year = (int(u_month) + c_month ) / 12
      rest_month = (int(u_month) + c_month ) % 12
      if rest_year == 1:
        rest_year = 0
      if rest_month == 0:
        rest_month = 12
      print(int(add_year), rest_month)
      expireDate = date(int(u_year)+int(add_year)+int(rest_year), int(rest_month), int(u_day))
      print(expireDate)
      if today >= expireDate:
        answer.append(i+1)
    return answer
# 테스트 1 〉	통과 (0.04ms, 10.4MB)
# 테스트 2 〉	통과 (0.10ms, 10.4MB)
# 테스트 3 〉	통과 (0.05ms, 10.5MB)
# 테스트 4 〉	통과 (0.04ms, 10.5MB)
# 테스트 5 〉	통과 (0.06ms, 10.4MB)
# 테스트 6 〉	통과 (0.08ms, 10.5MB)
# 테스트 7 〉	통과 (0.11ms, 10.4MB)
# 테스트 8 〉	통과 (0.14ms, 10.5MB)
# 테스트 9 〉	통과 (0.33ms, 10.5MB)
# 테스트 10 〉	통과 (0.18ms, 10.5MB)
# 테스트 11 〉	통과 (0.28ms, 10.4MB)
# 테스트 12 〉	통과 (0.30ms, 10.5MB)
# 테스트 13 〉	통과 (0.33ms, 10.5MB)
# 테스트 14 〉	통과 (0.33ms, 10.6MB)
# 테스트 15 〉	통과 (0.18ms, 10.4MB)
# 테스트 16 〉	통과 (0.48ms, 10.4MB)
# 테스트 17 〉	통과 (0.34ms, 10.5MB)
# 테스트 18 〉	통과 (0.33ms, 10.4MB)
# 테스트 19 〉	통과 (0.53ms, 10.4MB)
# 테스트 20 〉	통과 (0.36ms, 10.4MB)

# "모든 달은 28일까지 있다고 가정합니다."를 못보고 넘겨서...한세월을 풀었구나....ㅎㅎㅎㅎ.....
# 28일이면 date객체까지 갈 필요도 없었는데..

# 다시 풀기
def solution(today, terms, privacies):
    y, m, d = today.split('.')
    today = int(y) * 12 * 28 + int(m) * 28 + int(d)
    terms_obj = {}
    for t in terms:
      term_id, term_month = t.split(' ')
      terms_obj[term_id] = int(term_month) * 28
  
    answer = []
    for i, u in enumerate(privacies):
      u_date, term = u.split(' ')
      u_year, u_month, u_day = u_date.split('.')
      u_days = int(u_year) * 12 * 28 + int(u_month) * 28 + int(u_day)
      print(u_days)
      if u_days + terms_obj[term] <= today:
        answer.append(i + 1)
    return answer
  
# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.06ms, 10.5MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (0.05ms, 10.4MB)
# 테스트 5 〉	통과 (0.06ms, 10.3MB)
# 테스트 6 〉	통과 (0.06ms, 10.4MB)
# 테스트 7 〉	통과 (0.07ms, 10.5MB)
# 테스트 8 〉	통과 (0.04ms, 10.5MB)
# 테스트 9 〉	통과 (0.13ms, 10.4MB)
# 테스트 10 〉	통과 (0.14ms, 10.4MB)
# 테스트 11 〉	통과 (0.14ms, 10.2MB)
# 테스트 12 〉	통과 (0.14ms, 10.4MB)
# 테스트 13 〉	통과 (0.14ms, 10.5MB)
# 테스트 14 〉	통과 (0.17ms, 10.4MB)
# 테스트 15 〉	통과 (0.15ms, 10.4MB)
# 테스트 16 〉	통과 (0.25ms, 10.5MB)
# 테스트 17 〉	통과 (0.24ms, 10.3MB)
# 테스트 18 〉	통과 (0.27ms, 10.4MB)
# 테스트 19 〉	통과 (0.23ms, 10.4MB)
# 테스트 20 〉	통과 (0.23ms, 10.4MB)

# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
# print(solution("2020.12.17", ["A 12"], ["2010.01.01 A", "2019.12.17 A"])) # [1, 2]
# print(solution("2021.12.08", ["A 18"],  ["2020.06.08 A"])) # [1]



# 다른 사람 풀이 1
# 일로 변경해서 계산
def to_days(date):
    year, month, day = map(int, date.split(".")) # date를 분할해서  정수로 바꿈
    return year * 28 * 12 + month * 28 + day # 일로 바꿈

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms} # term의 2자리(개월 수)를 일로 바꿔서 term의 알파벳을 키로 담는다.
    today = to_days(today) # 오늘을 일수로 바꾼다.
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today # privacies의 날짜를 일수로 바꿔서 해당 term에 해당하는 일수를 더한다음 오늘보다 작거나 같으면 반환
    ]
    return expire
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (0.03ms, 10.5MB)
# 테스트 5 〉	통과 (0.05ms, 10.4MB)
# 테스트 6 〉	통과 (0.07ms, 10.3MB)
# 테스트 7 〉	통과 (0.04ms, 10.5MB)
# 테스트 8 〉	통과 (0.04ms, 10.5MB)
# 테스트 9 〉	통과 (0.07ms, 10.4MB)
# 테스트 10 〉	통과 (0.13ms, 10.4MB)
# 테스트 11 〉	통과 (0.13ms, 10.4MB)
# 테스트 12 〉	통과 (0.21ms, 10.4MB)
# 테스트 13 〉	통과 (0.22ms, 10.4MB)
# 테스트 14 〉	통과 (0.14ms, 10.3MB)
# 테스트 15 〉	통과 (0.12ms, 10.3MB)
# 테스트 16 〉	통과 (0.12ms, 10.4MB)
# 테스트 17 〉	통과 (0.25ms, 10.4MB)
# 테스트 18 〉	통과 (0.22ms, 10.4MB)
# 테스트 19 〉	통과 (0.20ms, 10.3MB)
# 테스트 20 〉	통과 (0.13ms, 10.5MB)



# 다른 사람 풀이 2
def solution(today, terms, privacies):
    answer = []
    termdict = {}

    for term in terms:
        t = term.split(' ')
        termdict[t[0]] = int(t[1]) * 28 # term을 키, 개월을 일로 바꿔서 termdict에 저장

    t = today.split('.')
    d = 28 * 12 * int(t[0]) + 28 * int(t[1]) + int(t[2]) # 오늘을 일로 변경

    for p in range(len(privacies)):
        pret = privacies[p].split(' ')
        t = pret[0].split('.') # 데이터의 날짜
        nd = 28 * 12 * int(t[0]) + 28 * int(t[1]) + int(t[2]) # 날짜를 일로 변경

        if termdict[pret[1]] + nd <= d: # term의 일수와 데이터의 일수를 더했을 때 오늘보다 같거나 작으면
            answer.append(p + 1) # 추가


    return answer
# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.06ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (0.04ms, 10.5MB)
# 테스트 5 〉	통과 (0.03ms, 10.4MB)
# 테스트 6 〉	통과 (0.05ms, 10.4MB)
# 테스트 7 〉	통과 (0.07ms, 10.4MB)
# 테스트 8 〉	통과 (0.04ms, 10.4MB)
# 테스트 9 〉	통과 (0.13ms, 10.4MB)
# 테스트 10 〉	통과 (0.12ms, 10.5MB)
# 테스트 11 〉	통과 (0.07ms, 10.4MB)
# 테스트 12 〉	통과 (0.17ms, 10.4MB)
# 테스트 13 〉	통과 (0.12ms, 10.3MB)
# 테스트 14 〉	통과 (0.15ms, 10.4MB)
# 테스트 15 〉	통과 (0.12ms, 10.4MB)
# 테스트 16 〉	통과 (0.14ms, 10.4MB)
# 테스트 17 〉	통과 (0.22ms, 10.4MB)
# 테스트 18 〉	통과 (0.21ms, 10.3MB)
# 테스트 19 〉	통과 (0.18ms, 10.4MB)
# 테스트 20 〉	통과 (0.23ms, 10.4MB)