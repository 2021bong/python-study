def solution(players, callings):
    ranking = {}
    for i, p in enumerate(players):
      ranking[p] = i + 1
      ranking[i+1] = p
    for c in callings:
      cur_rank = ranking[c]
      new_rank = cur_rank - 1
      front_player = ranking[new_rank]
      ranking[new_rank] = c
      ranking[cur_rank] = front_player
      ranking[c] = new_rank
      ranking[front_player] = cur_rank
    final = []
    for i in range(len(players)):
      final.append(ranking[i+1])
      
    return final
# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.08ms, 10.2MB)
# 테스트 4 〉	통과 (0.49ms, 10.3MB)
# 테스트 5 〉	통과 (1.78ms, 10.7MB)
# 테스트 6 〉	통과 (3.71ms, 10.8MB)
# 테스트 7 〉	통과 (22.56ms, 14.8MB)
# 테스트 8 〉	통과 (52.59ms, 19.5MB)
# 테스트 9 〉	통과 (292.34ms, 29.1MB)
# 테스트 10 〉	통과 (629.29ms, 61.7MB)
# 테스트 11 〉	통과 (1134.86ms, 96.5MB)
# 테스트 12 〉	통과 (707.73ms, 96.6MB)
# 테스트 13 〉	통과 (692.67ms, 96.4MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)

# 객체에 집착하느라 배열을 바꾸면 됐는데 생각을 못했다
# 다시 풀기
def solution(players, callings):
    ranking = {}
    for i, p in enumerate(players):
      ranking[p] = i
    for c in callings:
      cur_rank = ranking[c]
      ranking[c] -= 1
      ranking[players[cur_rank - 1]] += 1
      players[cur_rank], players[cur_rank - 1] = players[cur_rank - 1], players[cur_rank]
      
    return players
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.08ms, 10.4MB)
# 테스트 4 〉	통과 (0.43ms, 10.2MB)
# 테스트 5 〉	통과 (3.69ms, 10.7MB)
# 테스트 6 〉	통과 (4.66ms, 10.9MB)
# 테스트 7 〉	통과 (44.20ms, 14.5MB)
# 테스트 8 〉	통과 (61.91ms, 18.8MB)
# 테스트 9 〉	통과 (124.45ms, 27.8MB)
# 테스트 10 〉	통과 (344.33ms, 56.7MB)
# 테스트 11 〉	통과 (832.36ms, 91.6MB)
# 테스트 12 〉	통과 (1065.57ms, 91.6MB)
# 테스트 13 〉	통과 (1067.59ms, 91.6MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
  
# print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))



# 다른 사람 풀이
# 배열 자체를 바꾼 사람도 있고, 선수가 key, 등수가 key 객체 2개를 만들어서 바꾼 사람도 있다.
def solution(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)} # {선수 : 등수} 형태로 선수들 저장

    for p in callings:
        c = pla_dic[p] # 불린 선수의 등수 c
        pla_dic[p] -= 1 # 불린 선수의 등수를 하나 낮춘다.
        pla_dic[players[c-1]] += 1 # 불린 선수의 앞 선수 이름을 key로 넣어서 찾고 등수를 하나 올린다.
        players[c-1], players[c] = players[c], players[c-1] # 불린 선수와 제껴진 선수의 위치를 바꾼다.

    return players
# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.07ms, 10.3MB)
# 테스트 4 〉	통과 (0.36ms, 10.4MB)
# 테스트 5 〉	통과 (2.33ms, 10.6MB)
# 테스트 6 〉	통과 (4.91ms, 10.8MB)
# 테스트 7 〉	통과 (22.78ms, 14.4MB)
# 테스트 8 〉	통과 (57.39ms, 19MB)
# 테스트 9 〉	통과 (131.48ms, 28MB)
# 테스트 10 〉	통과 (531.63ms, 56.7MB)
# 테스트 11 〉	통과 (940.01ms, 91.6MB)
# 테스트 12 〉	통과 (968.42ms, 91.5MB)
# 테스트 13 〉	통과 (1237.00ms, 91.5MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
