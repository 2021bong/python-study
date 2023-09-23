def solution(progresses, speeds):
    days = [0] * len(progresses)
    for i, p in enumerate(progresses):
      while p < 100:
        p += speeds[i]
        days[i] += 1
    deploy = []
    ans = []
    for d in days:
      if len(deploy) == 0:
        deploy.append(d)
      else:
        if deploy[0] >= d:
          deploy.append(d)
        else:
          ans.append(len(deploy))
          deploy = []
          deploy.append(d)
    ans.append(len(deploy))
    return ans
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.22ms, 10.2MB)
# 테스트 4 〉	통과 (0.13ms, 9.96MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.14ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10MB)
# 테스트 9 〉	통과 (0.08ms, 10.3MB)
# 테스트 10 〉	통과 (0.09ms, 9.96MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)

# while 안쓰고 다시 풀기
def solution(progresses, speeds):
    days = []
    for i, p in enumerate(progresses):
      days.append(-((p-100) // speeds[i]))
    deploy = []
    ans = []
    for d in days:
      if len(deploy) == 0:
        deploy.append(d)
      else:
        if deploy[0] >= d:
          deploy.append(d)
        else:
          ans.append(len(deploy))
          deploy = []
          deploy.append(d)
    ans.append(len(deploy))
    return ans
# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.05ms, 10.1MB)
# 테스트 3 〉	통과 (0.04ms, 10.1MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.02ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
    
# print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # [1, 3, 2]
# print(solution([90, 98, 97, 96, 98], [1, 1, 1, 1, 1])) # [5]


# 다른 사람 풀이
def solution(progresses, speeds):
    Q=[] # [걸리는 일 수, 배포가능한 개수]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): # Q가 비어있거나, Q의 가장 마지막 요소의 걸리는 일수(Q[-1][0])가 비교하는 p의 걸리는 일수보다 작으면
            Q.append([-((p-100)//s),1]) # [걸리는 일수, 1]를 Q에 추가
        else:
            Q[-1][1]+=1 # Q가 있거나, Q의 가장 마지막 요소의 걸리는 일수가 더 크다면 배포가능한 개수를 추가한다.
    return [q[1] for q in Q] # 배포가능한 개수만을 남긴 배열을 반환한다.
  
# print((93-100)//4) # -2
# print((100-93)//4) # 1
# 이렇게 되므로 -((p-100)//s 을 사용한 것 같음

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.02ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 9.99MB)

