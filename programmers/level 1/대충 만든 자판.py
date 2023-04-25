# 대충 만든 자판

def solution(keymap, targets):
  keypad = {}
  for i in keymap:
    for j in range(len(i)):
      if i[j] in keypad:
        mincount = min(keypad[i[j]], i.index(i[j])+1)
        keypad[i[j]] = mincount
      else:
        keypad[i[j]] = i.index(i[j]) + 1
      
  answer = []
  for i in targets:
    count = 0
    for j in i:
      if j in keypad:
        count += keypad[j]
      else:
        count = 0
        answer.append(-1)
        break
    if count != 0:
      answer.append(count)
  return answer
# 테스트 1 〉	통과 (0.22ms, 10MB)
# 테스트 2 〉	통과 (0.32ms, 10.2MB)
# 테스트 3 〉	통과 (0.14ms, 10.1MB)
# 테스트 4 〉	통과 (0.25ms, 10.1MB)
# 테스트 5 〉	통과 (0.16ms, 9.99MB)
# 테스트 6 〉	통과 (0.26ms, 10.1MB)
# 테스트 7 〉	통과 (0.16ms, 10.2MB)
# 테스트 8 〉	통과 (0.20ms, 10.2MB)
# 테스트 9 〉	통과 (0.12ms, 10.1MB)
# 테스트 10 〉	통과 (0.19ms, 9.98MB)
# 테스트 11 〉	통과 (0.03ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (1.82ms, 10.2MB)
# 테스트 15 〉	통과 (1.80ms, 10.2MB)
# 테스트 16 〉	통과 (2.12ms, 10.1MB)
# 테스트 17 〉	통과 (1.93ms, 10.2MB)
# 테스트 18 〉	통과 (1.16ms, 10.1MB)
# 테스트 19 〉	통과 (1.71ms, 10.2MB)
# 테스트 20 〉	통과 (1.42ms, 10.2MB)
# 테스트 21 〉	통과 (1.82ms, 10.4MB)
# 테스트 22 〉	통과 (2.28ms, 10.3MB)
# 테스트 23 〉	통과 (1.90ms, 10.1MB)
  
# print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"])) # [9, 4]
# print(solution(["AA"], ["B"])) # [-1]
# print(solution(["AGZ", "BSSS"], ["ASA","BGZ"])) # [4, 6]
# print(solution(["ABCE"], ["ABDE"])) # [-1]
# print(solution(["ABCDE","ABBCE"], ["ABBEF"])) # [-1]
# print(solution(["ABCDEFGHIJK"], ["J"])) # [10]
# print(solution(["FFF", "FFF"], ["CCC", "CCC"])) # [-1, -1]
# print(solution(["AGZ", "BSSS"], ["AGY", "BSSS"])) # [-1, 7]
# print(solution(["A"], ["A","B"])) # [1,-1]
# print(solution(["AA"], ["BA"])) # [-1]
# print(solution(["BCE"], ["ABC"])) # [-1]
# print(solution(["BCC"], ["ABC"])) # [-1]
# print(solution(["ABACD", "BCEFD"], ["XABCD", "AABB"])) # [-1, 4]


# 다른 사람 풀이 1
def solution(keymap, targets):
    answer = []
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1 # 최솟값도 한번에 넣는다.

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs: # 만들어둔 hs에 해당 글자(ch)가 없으면
                ret = - 1 # ret을 -1로 만들고 반복문을 종료한다.
                break
            ret += hs[ch] # ret에 키패드의 값을 누적한다.
        answer.append(ret) # targets의 요소의 글자를 다 돌고나면 답에 ret을 추가한다.

    return answer
# 테스트 1 〉	통과 (0.14ms, 10.2MB)
# 테스트 2 〉	통과 (0.22ms, 10.2MB)
# 테스트 3 〉	통과 (0.14ms, 10.2MB)
# 테스트 4 〉	통과 (0.16ms, 10.2MB)
# 테스트 5 〉	통과 (0.11ms, 10.2MB)
# 테스트 6 〉	통과 (0.18ms, 10.2MB)
# 테스트 7 〉	통과 (0.11ms, 10.2MB)
# 테스트 8 〉	통과 (0.23ms, 10.2MB)
# 테스트 9 〉	통과 (0.16ms, 10.1MB)
# 테스트 10 〉	통과 (0.10ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (0.96ms, 10.2MB)
# 테스트 15 〉	통과 (1.15ms, 10.2MB)
# 테스트 16 〉	통과 (1.34ms, 10.3MB)
# 테스트 17 〉	통과 (1.12ms, 10.1MB)
# 테스트 18 〉	통과 (0.73ms, 10.1MB)
# 테스트 19 〉	통과 (1.17ms, 10.1MB)
# 테스트 20 〉	통과 (0.88ms, 10.2MB)
# 테스트 21 〉	통과 (1.13ms, 10.3MB)
# 테스트 22 〉	통과 (1.12ms, 10.1MB)
# 테스트 23 〉	통과 (1.01ms, 10.3MB)
  
  
# 다른 사람 풀이 2
def solution(keymap, targets):
    answer = []
    #최솟값 저장
    alpha = [101 for i in range(26)] # 알파벳의 개수만큼 101이 담긴 리스트를 만든다.
    for i in keymap:
        for idx, j in enumerate(i):
            k = ord(j)-ord('A') # alpha에서 문자(j)의 인덱스를 찾기위해 j와 'A'의 아스키코드 차를 구한다.
            alpha[k] = min(alpha[k],idx+1) # 101과 눌러야하는 키패드의 횟수중에 더 작은것으로 alpha에 해당 문자의 값을 변경한다.

    for i in targets:
        total = 0 # 반복문을 다 돌아야하므로 시작할땐 total을 0으로 초기화시켜준다.
        for j in i:
            cnt = alpha[ord(j) - ord('A')] # 키패드를 몇 번 눌러야하는지 값을 찾는다.
            if cnt ==101: # cnt가 101이면 이 문자는 없다는 뜻이다.
                answer.append(-1) # -1을 넣고 반복문을 종료한다.
                break
            else:
                total+= cnt # 있는 문자라면 total에 값을 누적시킨다.
        else:
            answer.append(total) # targets[i]에 대한 키패드 값을 answer에 추가한다.



    return answer
# 테스트 1 〉	통과 (0.19ms, 10.2MB)
# 테스트 2 〉	통과 (0.18ms, 10.3MB)
# 테스트 3 〉	통과 (0.14ms, 10.2MB)
# 테스트 4 〉	통과 (0.37ms, 10.2MB)
# 테스트 5 〉	통과 (0.15ms, 9.98MB)
# 테스트 6 〉	통과 (0.51ms, 10.2MB)
# 테스트 7 〉	통과 (0.26ms, 10.3MB)
# 테스트 8 〉	통과 (0.17ms, 10.2MB)
# 테스트 9 〉	통과 (0.22ms, 10.2MB)
# 테스트 10 〉	통과 (0.13ms, 10.2MB)
# 테스트 11 〉	통과 (0.05ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (2.54ms, 10.2MB)
# 테스트 15 〉	통과 (1.80ms, 10.2MB)
# 테스트 16 〉	통과 (1.64ms, 10.2MB)
# 테스트 17 〉	통과 (1.62ms, 10.4MB)
# 테스트 18 〉	통과 (1.87ms, 10.1MB)
# 테스트 19 〉	통과 (1.46ms, 10.3MB)
# 테스트 20 〉	통과 (0.94ms, 10.3MB)
# 테스트 21 〉	통과 (1.54ms, 10.3MB)
# 테스트 22 〉	통과 (1.45ms, 10.2MB)
# 테스트 23 〉	통과 (1.32ms, 10.1MB)
  
  
# 다른 사람 풀이 3
def solution(keymap, targets):
    answer = []

    for target in targets:
        c = 0
        for t in target: # x = keymap[i], t = targets[k][l]
            r = min(list(map((lambda x: x.index(t) + 1 if t in x else 102), keymap))) # t가 x에 있으면 t의 인덱스 + 1, 없으면 102 -> 중에 작은 값
            if r == 102:
                answer.append(-1)
                break
            else:
                c += r
        if r != 102:
            answer.append(c)          

    return answer
# 테스트 1 〉	통과 (2.12ms, 10.1MB)
# 테스트 2 〉	통과 (2.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.80ms, 10.3MB)
# 테스트 4 〉	통과 (2.04ms, 10.3MB)
# 테스트 5 〉	통과 (0.78ms, 10.3MB)
# 테스트 6 〉	통과 (1.40ms, 10.2MB)
# 테스트 7 〉	통과 (0.55ms, 10.2MB)
# 테스트 8 〉	통과 (0.96ms, 10.4MB)
# 테스트 9 〉	통과 (0.40ms, 10.3MB)
# 테스트 10 〉	통과 (0.79ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)
# 테스트 14 〉	통과 (20.93ms, 10.2MB)
# 테스트 15 〉	통과 (39.51ms, 10.3MB)
# 테스트 16 〉	통과 (46.45ms, 10.1MB)
# 테스트 17 〉	통과 (34.79ms, 10.1MB)
# 테스트 18 〉	통과 (17.00ms, 10.2MB)
# 테스트 19 〉	통과 (20.27ms, 10.2MB)
# 테스트 20 〉	통과 (17.20ms, 10.1MB)
# 테스트 21 〉	통과 (19.48ms, 10.2MB)
# 테스트 22 〉	통과 (23.44ms, 10.3MB)
# 테스트 23 〉	통과 (43.00ms, 10.3MB)
# r을 구할때 무조건 n번 반복해서 시간이 오래 걸리는 것 같다.