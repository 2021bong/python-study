# 옹알이 (2)

def solution(babbling):
    baby_can = ["aya", "ye", "woo", "ma"]
    baby_can_double = ["ayaaya", "yeye", "woowoo", "mama"]
    for i in range(len(babbling)):
      for j in baby_can_double:
        if j in babbling[i]:
          babbling[i] = 'False'
          continue
    for i in range(len(babbling)):
      for c in baby_can:
        if c in babbling[i]:
          babbling[i] = babbling[i].replace(c, '*')
    babbling = [i.replace('*','') for i in babbling]
    return len([i for i in babbling if i == ''])
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.07ms, 10.3MB)
# 테스트 13 〉	통과 (0.11ms, 10.3MB)
# 테스트 14 〉	통과 (0.10ms, 10.3MB)
# 테스트 15 〉	통과 (0.06ms, 10.4MB)
# 테스트 16 〉	통과 (0.12ms, 10.3MB)
# 테스트 17 〉	통과 (0.08ms, 10.2MB)
# 테스트 18 〉	통과 (0.05ms, 10.2MB)
# 테스트 19 〉	통과 (0.05ms, 10.2MB)
# 테스트 20 〉	통과 (0.06ms, 10.3MB)
  
# print(solution(["aya", "yee", "u", "maa"]))
# print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
# print(solution(["woayao"])) # 0
# print(solution(["wooyemawooye", "mayaa", "ymaeaya"])) # 1


# 다른 사람 풀이 1
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i: # 연속되는 음절이 없을때
                i=i.replace(j,' ') # 해당 단어를 공백으로 처리
        if len(i.strip())==0: # 단어가 빈문자열이면
            answer +=1 # 정답 count + 1
    return answer
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 9.98MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.02ms, 10.3MB)
# 테스트 11 〉	통과 (0.04ms, 9.99MB)
# 테스트 12 〉	통과 (0.13ms, 10.1MB)
# 테스트 13 〉	통과 (0.11ms, 10.2MB)
# 테스트 14 〉	통과 (0.09ms, 10.2MB)
# 테스트 15 〉	통과 (0.10ms, 10.1MB)
# 테스트 16 〉	통과 (0.10ms, 10.1MB)
# 테스트 17 〉	통과 (0.09ms, 10.3MB)
# 테스트 18 〉	통과 (0.07ms, 10.1MB)
# 테스트 19 〉	통과 (0.03ms, 10.3MB)
# 테스트 20 〉	통과 (0.06ms, 10.1MB)
  
  
# 다른 사람 풀이 2
def solution(babbling):
    count = 0

    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b: # 아예 반복문에서 연속음이 걸리면 반복문 다음 횟수로 넘어가고
            continue    
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""): # 발음 가능한 단어를 다 빈문자열로 바꿨는데 빈문자열이면
            count += 1 # 정답 count + 1

    return count
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10MB)
# 테스트 4 〉	통과 (0.00ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 9.98MB)
# 테스트 7 〉	통과 (0.00ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.03ms, 10.1MB)
# 테스트 13 〉	통과 (0.07ms, 10.1MB)
# 테스트 14 〉	통과 (0.06ms, 10MB)
# 테스트 15 〉	통과 (0.02ms, 10MB)
# 테스트 16 〉	통과 (0.06ms, 10.2MB)
# 테스트 17 〉	통과 (0.04ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 테스트 19 〉	통과 (0.02ms, 10.4MB)
# 테스트 20 〉	통과 (0.04ms, 10.2MB)