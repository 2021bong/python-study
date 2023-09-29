def solution(priorities, location):
    processes = []
    target = ""
    for i, p in enumerate(priorities):
        processes.append([i, p])
        if i == location:
            target = i
    count = 0
    while len(processes) != 0:
        max_index = [i[1] for i in processes].index(
            max([i[1] for i in processes]))
        if processes[max_index][0] == target:
            count += 1
            break
        go_back = processes[0:max_index]
        go_front = processes[max_index+1:]
        processes = go_front + go_back
        count += 1
    return count
# 테스트 1 〉	통과 (0.74ms, 10.1MB)
# 테스트 2 〉	통과 (0.62ms, 10.1MB)
# 테스트 3 〉	통과 (0.08ms, 10.2MB)
# 테스트 4 〉	통과 (0.05ms, 10.1MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.14ms, 10.2MB)
# 테스트 7 〉	통과 (0.08ms, 10.3MB)
# 테스트 8 〉	통과 (0.46ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.10ms, 10.2MB)
# 테스트 11 〉	통과 (0.34ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.1MB)
# 테스트 13 〉	통과 (0.27ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.04ms, 10.2MB)
# 테스트 17 〉	통과 (0.39ms, 10.3MB)
# 테스트 18 〉	통과 (0.03ms, 10.1MB)
# 테스트 19 〉	통과 (0.41ms, 10.3MB)
# 테스트 20 〉	통과 (0.06ms, 10.1MB)

# print(solution([2, 1, 3, 2], 2))  # 1
# print(solution([1, 1, 9, 1, 1, 1], 0))  # 5


# 다른 사람 풀이 1
# any() : 하나라도 True인게 있으면 True를 반환
def solution(priorities, location):
    # (최초 인덱스, 우선 순위)로 배열을 큐를 만듦
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)  # 큐에서 0번째를 꺼냄
        if any(cur[1] < q[1] for q in queue):  # cur보다 우선순위가 큰게 있으면
            queue.append(cur)  # cur을 제일 뒤로 보냄
        else:
            answer += 1  # 프로세스 실행 횟수 추가
            if cur[0] == location:  # cur가 location으로 들어온 프로세스면
                return answer  # 실행 횟수 리턴
# 테스트 1 〉	통과 (0.55ms, 10.1MB)
# 테스트 2 〉	통과 (1.30ms, 10.1MB)
# 테스트 3 〉	통과 (0.05ms, 10.1MB)
# 테스트 4 〉	통과 (0.05ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.22ms, 10.2MB)
# 테스트 7 〉	통과 (0.09ms, 10.2MB)
# 테스트 8 〉	통과 (0.52ms, 10.1MB)
# 테스트 9 〉	통과 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (0.22ms, 10.1MB)
# 테스트 11 〉	통과 (0.77ms, 10.2MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.35ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.11ms, 10.2MB)
# 테스트 17 〉	통과 (0.48ms, 10.2MB)
# 테스트 18 〉	통과 (0.04ms, 10.2MB)
# 테스트 19 〉	통과 (0.80ms, 10.1MB)
# 테스트 20 〉	통과 (0.12ms, 10.2MB)


# 다른 사람 풀이 2
def solution(p, l):
    ans = 0
    m = max(p)  # 제일 우선 순위가 높은 값
    while True:
        v = p.pop(0)  # p에서 0번째를 아예 빼면서 v에 값 할당
        if m == v:  # m이랑 v랑 같으면 가장 높은 우선 순위가 같으면
            ans += 1  # 프로세스 실행되므로 카운트 +1
            if l == 0:  # l이 0이면 바로 종료 *** 여기가 유일한 while 탈출 조건
                break
            else:  # 0이 아니면 -1
                l -= 1
            m = max(p)  # 우선순위 값 m 재할당
        else:
            p.append(v)  # p에서 제거했던 v를 맨 뒤에 다시 넣기
            if l == 0:  # l이 0이었다면 맨 뒤로 갔으므로
                l = len(p)-1  # len - 1로 재할당
            else:
                l -= 1  # 0이 아니면 -1
    return ans
# 테스트 1 〉	통과 (0.08ms, 10MB)
# 테스트 2 〉	통과 (0.18ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.13ms, 10MB)
# 테스트 9 〉	통과 (0.01ms, 10MB)
# 테스트 10 〉	통과 (0.07ms, 10.1MB)
# 테스트 11 〉	통과 (0.11ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.09ms, 10MB)
# 테스트 14 〉	통과 (0.01ms, 9.95MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.02ms, 10.1MB)
# 테스트 17 〉	통과 (0.13ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.1MB)
# 테스트 19 〉	통과 (0.10ms, 10MB)
# 테스트 20 〉	통과 (0.02ms, 10.1MB)
