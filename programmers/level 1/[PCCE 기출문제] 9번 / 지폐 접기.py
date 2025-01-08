import math


def solution(wallet, bill):
    answer = 0
    while min(wallet) < min(bill) or max(wallet) < max(bill):
        bill_i = bill.index(max(bill))
        bill[bill_i] = math.floor(bill[bill_i]/2)
        answer += 1
    return answer
# 테스트 1 〉	통과 (0.00ms, 10.4MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.3MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.1MB)
# 테스트 18 〉	통과 (0.02ms, 10.2MB)
# 테스트 19 〉	통과 (0.02ms, 10.2MB)
# 테스트 20 〉	통과 (0.02ms, 10.1MB)

# 참고해서 다시 풀이


def solution(wallet, bill):
    answer = 0
    while min(wallet) < min(bill) or max(wallet) < max(bill):
        bill_i = bill.index(max(bill))
        bill[bill_i] //= 2
        answer += 1
    return answer
# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.02ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 테스트 19 〉	통과 (0.02ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)

# print(solution([30,15],[26,17]))
# print(solution([50,50],[100,241]))

# 다른 사람 풀이 1


def solution(wallet, bill):

    wallet, bill = sorted(wallet), sorted(bill)  # [작은값, 큰값]으로 둘다 정렬
    cnt = 0
    while wallet[0] < bill[0] or wallet[1] < bill[1]:  # 가로세로 모두 지폐가 더 작을때까지
        bill[-1] //= 2  # -1로 큰 값을 무조건 2로 나눠서 몫만 재할당
        bill = sorted(bill)  # 다시 [작은값, 큰값]으로 정렬
        cnt += 1  # 접은 횟수 증가

    return cnt

# 다른 사람 풀이 2


def solution(wallet, bill):
    answer = 0

    while max(bill) > max(wallet) or min(bill) > min(wallet):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2  # 나랑 비슷한데 // 연산자 사용, 파이썬 오랜만이 연산자가 기억 안났음 ㅎ
        else:
            bill[1] = bill[1] // 2
        answer += 1

    return answer
