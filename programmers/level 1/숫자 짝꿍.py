# 숫자 짝꿍

def solution(X, Y):
    set_x = set([i for i in X])
    set_y = set([i for i in Y])
    f = set_x & set_y
    if len(f) == 0:
      return '-1'
    count = {}
    for i in f:
      x_count = X.count(i)
      y_count = Y.count(i)
      count[i] = x_count if x_count < y_count else y_count
    if '0' in count and len(count.keys()) == 1:
      return '0'
    friends = sorted(list(count.keys()), reverse=True)
    answer = ''
    for i in friends:
      answer += i * count[i]
    return answer
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.10ms, 10.2MB)
# 테스트 7 〉	통과 (0.05ms, 10.2MB)
# 테스트 8 〉	통과 (0.07ms, 10.2MB)
# 테스트 9 〉	통과 (0.07ms, 10.4MB)
# 테스트 10 〉	통과 (0.05ms, 10.3MB)
# 테스트 11 〉	통과 (271.21ms, 46MB)
# 테스트 12 〉	통과 (268.93ms, 46MB)
# 테스트 13 〉	통과 (233.22ms, 46MB)
# 테스트 14 〉	통과 (243.74ms, 45.9MB)
# 테스트 15 〉	통과 (276.81ms, 45.9MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
    
# print(solution('100','2345'))
# print(solution('100','203045'))
# print(solution('100','123450'))
# print(solution('12321','42531'))
# print(solution('5525','1255'))


# 다른 사람 풀이 1
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) : # 9부터 -1씩 0까지
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i)))) # X랑 Y에서 숫자를 세서 더 작은 갯수만큼 숫자를 더해서 answer에 더함
        # answer += 9 * (X의 9의 개수와 Y의 9의 개수 중)더 작은 것 -> 그러면 만들 수 있는 수중에 제일 큰 수가 만들어짐

    if answer == '' : # 짝꿍이 없을 때
        return '-1'
    elif len(answer) == answer.count('0'): # 0 밖에 없을 때
        return '0'
    else :
        return answer
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.1MB)
# 테스트 6 〉	통과 (0.03ms, 10.1MB)
# 테스트 7 〉	통과 (0.03ms, 10.1MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.1MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (85.78ms, 27.5MB)
# 테스트 12 〉	통과 (93.02ms, 27.6MB)
# 테스트 13 〉	통과 (88.08ms, 27.7MB)
# 테스트 14 〉	통과 (86.74ms, 27.6MB)
# 테스트 15 〉	통과 (90.01ms, 27.6MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)
# 테스트 17 〉	통과 (0.01ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 테스트 19 〉	통과 (0.02ms, 10.2MB)



# 다른 사람 풀이 2
def solution(X, Y):
    li1 = [0]*10 # 길이가 10인 배열을 만든다. 0부터 9까지 -> 10개
    li2 = [0]*10
    for i in X:
        li1[int(i)] += 1 # X를 돌면서 아까 만든 배열에 숫자를 카운트해준다.
    for i in Y:
        li2[int(i)] += 1
    for i in range(10): # 카운트 해 놓은 배열에서 작은 수를 li1의 값으로 바꾼다.
        li1[i] = min(li1[i],li2[i])
    answer = ''
    count = 0
    for i in range(9,-1,-1): # 9부터 거꾸로 돌면서
        if li1[i] == 0 and i != 0: count += 1 # 세어놓은 카운트가 0이면서 찾는 숫자가 0이 아닐때 count를 1 올려준다.
        answer += str(i) * li1[i] # 아닐때는 정답에 숫자를 더한다.
    if not answer: return "-1" # answer가 비었을 땐 -1
    if count == 9: return "0" # count가 9일때는 0밖에 없다고 판단하여 0 반환
    return answer
# 테스트 1 〉	통과 (0.04ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.04ms, 10.4MB)
# 테스트 5 〉	통과 (0.04ms, 10.4MB)
# 테스트 6 〉	통과 (0.24ms, 10.3MB)
# 테스트 7 〉	통과 (0.30ms, 10.4MB)
# 테스트 8 〉	통과 (0.29ms, 10.4MB)
# 테스트 9 〉	통과 (0.17ms, 10.4MB)
# 테스트 10 〉	통과 (0.16ms, 10.3MB)
# 테스트 11 〉	통과 (1073.60ms, 27.7MB) # 굉장한 시간...
# 테스트 12 〉	통과 (1086.19ms, 27.9MB)
# 테스트 13 〉	통과 (968.24ms, 27.8MB)
# 테스트 14 〉	통과 (1199.31ms, 27.8MB)
# 테스트 15 〉	통과 (1042.30ms, 27.8MB)
# 테스트 16 〉	통과 (0.03ms, 10.2MB)
# 테스트 17 〉	통과 (0.03ms, 10.5MB)
# 테스트 18 〉	통과 (0.03ms, 10.5MB)
# 테스트 19 〉	통과 (0.03ms, 10.3MB)