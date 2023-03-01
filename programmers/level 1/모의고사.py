# 모의고사

# 1번 수포자 1, 2, 3, 4, 5
# 2번 수포자 2, 1, 2, 3, 2, 4, 2, 5
# 3번 수포자 3, 3, 1, 1, 2, 2, 4, 4, 5, 5

# 첫번째 풀이
def solution(answers):
    ans = ['12345', '21232425', '3311224455']
    correct = [0, 0, 0]
    for i in range(len(correct)):
      for j in range(len(answers)):
        if answers[j] == int((ans[i][j % len(ans[i])])):
          correct[i] += 1
    winner = []
    for i in range(len(correct)):
      if max(correct) == correct[i]:
        winner.append(i+1)
    return winner
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.1MB)
# 테스트 5 〉	통과 (0.06ms, 10.4MB)
# 테스트 6 〉	통과 (0.10ms, 10.1MB)
# 테스트 7 〉	통과 (6.46ms, 10.3MB)
# 테스트 8 〉	통과 (1.29ms, 10.2MB)
# 테스트 9 〉	통과 (7.08ms, 10.4MB)
# 테스트 10 〉	통과 (3.40ms, 10.2MB)
# 테스트 11 〉	통과 (11.58ms, 10.3MB)
# 테스트 12 〉	통과 (11.38ms, 10.4MB)
# 테스트 13 〉	통과 (0.39ms, 10.3MB)
# 테스트 14 〉	통과 (7.23ms, 10.3MB)

# 다른 사람 풀이 참고
def solution(answers):
    ans = [[1, 2, 3, 4, 5],
          [2, 1, 2, 3, 2, 4, 2, 5],
          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]] # 문자열의 인덱스보다 리스트의 인덱스에 접근하는게 효율이 좋다. 애초에 숫자로 비교하면 int형으로 바꿔 줄 필요가 없다.
    correct = [0, 0, 0]
    for i, a in enumerate(ans): # enumerate를 사용해서 한번에 비교하니 효율이 훨씬 좋아졌다.
      for j, c in enumerate(answers):
        if c == a[j % len(a)]:
          correct[i] += 1
    return [i+1 for i in range(3) if max(correct) == correct[i]] # 한 줄로 바꾸니까 효율이 좋아지는 것 같은데 확실히는 잘 모르겠다.
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10MB)
# 테스트 3 〉	통과 (0.02ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.03ms, 10.1MB)
# 테스트 7 〉	통과 (1.62ms, 10.2MB)
# 테스트 8 〉	통과 (0.55ms, 10.2MB)
# 테스트 9 〉	통과 (3.12ms, 10.4MB)
# 테스트 10 〉	통과 (1.46ms, 10.3MB)
# 테스트 11 〉	통과 (3.17ms, 10.1MB)
# 테스트 12 〉	통과 (2.90ms, 10.3MB)
# 테스트 13 〉	통과 (0.18ms, 10.3MB)
# 테스트 14 〉	통과 (3.28ms, 10.2MB)
  
# print(solution([1,2,3,4,5]))
# print(solution([1,3,2,4,2]))
# print(solution([1,1,1,1,1,1,1,1,1,1])) # [1, 2, 3]
# print(solution([1,3,2,1,3,2,1])) # [3]
# print(solution([5,5,5,5,4])) # [1, 2, 3]

# 다른 사람 풀이 1
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers): # enumerate를 써서 이중 for문을 돌리지않고 3개 다 한번에 비교한다.
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.04ms, 10MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (2.80ms, 10.1MB)
# 테스트 8 〉	통과 (0.58ms, 10MB)
# 테스트 9 〉	통과 (2.99ms, 10.2MB)
# 테스트 10 〉	통과 (2.45ms, 10.1MB)
# 테스트 11 〉	통과 (2.96ms, 10.3MB)
# 테스트 12 〉	통과 (4.66ms, 10.1MB)
# 테스트 13 〉	통과 (0.28ms, 10MB)
# 테스트 14 〉	통과 (3.01ms, 10.3MB)
  
# 다른 사람 풀이 2
def solution(answers):
    p = [[1, 2, 3, 4, 5],
          [2, 1, 2, 3, 2, 4, 2, 5],
          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)] # 답을 수포자의 번호로 바꿀때 [한줄for문]으로 하는 방법도 있다..!
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 9.92MB)
# 테스트 4 〉	통과 (0.01ms, 10MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.07ms, 9.9MB)
# 테스트 7 〉	통과 (2.29ms, 10.1MB)
# 테스트 8 〉	통과 (0.80ms, 10.1MB)
# 테스트 9 〉	통과 (4.19ms, 10.1MB)
# 테스트 10 〉	통과 (2.58ms, 10.1MB)
# 테스트 11 〉	통과 (4.75ms, 10.2MB)
# 테스트 12 〉	통과 (3.96ms, 9.98MB)
# 테스트 13 〉	통과 (0.33ms, 10.1MB)
# 테스트 14 〉	통과 (5.12ms, 10.1MB)
  
a = [15, 20, 20, 12, 1]
print([i + 1 for i, v in enumerate(a) if v == max(a)]) # [2, 3]
print(i + 1 for i, v in enumerate(a) if v == max(a)) # <generator object <genexpr> at 0x106e2c9e0>
# 조건 식 통과하면 할 행동 / for 변수 in 이터러블 / 조건식 (한줄 for문은 이렇게 쓰는건가...?)
# 배열이나 튜플같은 데이터타입으로 변경해줘야 값을 볼 수 있어서 다들 []로 감싸는 것 같다.