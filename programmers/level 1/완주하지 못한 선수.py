# 완주하지 못한 선수

def solution(participant, completion):
    if len(completion) == 0:
      return participant[0]
    p = {}
    for i in participant:
      if i not in p:
        p[i] = 1
      else:
        p[i] += 1
    for i in completion:
      if i in p:
        p[i] -= 1
    
    return [i[0] for i in p.items() if i[1] == 1][0]
# 배열+while로 풀었다가 시간초과 났는데 딕셔너리로 푸니까 뚝딱... 배열은 정말 느리구나...
    
# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
# print(solution(["leo"],[]))

# 다른 사람 풀이 1
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion) # 배열의 값을 key로 갯수를 세어줌 (사기...) 빼기도 됨..
    return list(answer.keys())[0]


# 다른 사람 풀이 2
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part # 해시함수 이용
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
# 파이썬의 해시테이블은 딕셔너리로 되어있다고 한다..
print(hash('hi')) # 3567364966015008095