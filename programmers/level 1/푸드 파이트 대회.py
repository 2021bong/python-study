# 푸드 파이트 대회

# 첫번째 풀이
# def solution(food):
#     answer = []
#     for i, f in enumerate(food):
#       if f > 1 and f % ((i+1)*2) >= 0:
#         answer.append(str(i) * (f // 2))
#     return ''.join(answer)+'0'+''.join(reversed(answer))
    

# 다른 사람 풀이 참고
def solution(food):
    answer = ''
    for i, f in enumerate(food):
        answer += str(i) * (f//2) # 어차피 몫이 0이면 문자열이 추가되지 않는다. (f가 1이나 0인 경우 해결)
    return answer + '0' + answer[::-1]

# print(solution([1, 3, 4, 6]))
# print(solution([1, 7, 1, 2]))

# 다른 사람 풀이 1
# food 배열을 뒤에서부터 순회하면서 하나씩 answer에 좌우로 붙인다. 2개를 배치했으니 c(food 요소를 2로 나눈 몫)를 1 빼준다.
# 몫이 0보다 작으면 더이상 배치할 수 없으므로 다음 food 요소로 넘어간다.
def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer
  
# 다른 사람 풀이 2
def solution(food):
    answer = ''
    rev=''
    for i in range(1,len(food)):
        answer+=str(i)*(food[i]//2) # 문자열에 재할당 할 때 부터 문자열(food 요소의 순번) * 반복횟수(food 요소의 몫)를 할 수도 있겠다.
    rev=answer[::-1] # reversed()를 쓰지않고 슬라이싱을 이용하는 방법도 있다.
    answer+='0'

    return answer+rev
# print([1,2,3,4,5,6][::-1]) # [6, 5, 4, 3, 2, 1]