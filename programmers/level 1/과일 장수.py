# 과일 장수

# 11,12,13,14,15 시간초과
# def solution(k, m, score):
#     money = 0
#     score.sort()
#     while len(score) >= m:
#       length = len(score)
#       money += score[length-m::][0] * m
#       score = score[0:length-m:]
#     return money

def solution(k, m, score):
    money = 0
    score.sort(reverse=True)
    avg = score[m-1::m]
    for i in avg:
      money += i * m
    return money
# 슬라이싱을 잘 쓰자..! 슬라이싱 최고!!!

# print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
# print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))

# 다른 사람 풀이
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True) # 내림차순으로 정렬
    apple_box = []
    for i in range(0, len(score), m):
        apple_box.append(score[i:i+m]) # 사과 상자에 들어가는 개수만큼 score를 잘라 apple_box에 넣는다. apple_box는 이중 배열이 된다.
    for apple in apple_box:
        if len(apple) == m: # apple_box의 요소의 길이가 m과 같으면
            answer += min(apple) * m # 요소의 최소값과 m을 곱하고 answer에 더한다.

    return answer
