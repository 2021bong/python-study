cnt = 0
def dfs(numbers, target, idx, values):
    global cnt

    if idx == len(numbers) and values == target:
        cnt += 1
        return
    elif idx == len(numbers):
        return

    dfs(numbers, target, idx+1, values + numbers[idx])
    dfs(numbers, target, idx+1, values - numbers[idx])

def solution(numbers, target):
    global cnt
    dfs(numbers, target, 0, 0)

    return cnt
# 검색한 dfs 코드로 통과
# 테스트 1 〉	통과 (455.72ms, 10MB)
# 테스트 2 〉	통과 (476.21ms, 10.1MB)
# 테스트 3 〉	통과 (0.96ms, 10MB)
# 테스트 4 〉	통과 (1.64ms, 10.3MB)
# 테스트 5 〉	통과 (13.26ms, 10.2MB)
# 테스트 6 〉	통과 (0.88ms, 10.2MB)
# 테스트 7 〉	통과 (0.48ms, 10.2MB)
# 테스트 8 〉	통과 (3.28ms, 10.2MB)

# print(solution([1, 1, 1, 1, 1], 3))  # 5
# print(solution([4, 1, 2, 1], 4))  # 2