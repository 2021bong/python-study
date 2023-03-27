# 카드 뭉치

def solution(cards1, cards2, goal):
    num1 = -1
    num2 = -1
    for i in range(len(goal)):
      if goal[i] in cards1:
        if num1+1 != cards1.index(goal[i]):
          return 'No'
        num1 = cards1.index(goal[i])
      elif goal[i] in cards2:
        if num2+1 != cards2.index(goal[i]):
          return 'No'
        num2 = cards2.index(goal[i])
    return 'Yes'
# 풀면서 index()쓰면서 오래걸릴거라고는 생각했음ㅎㅎ.. 근데 goal 최대길이 20개라서 그냥 풀었다..
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.00ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10MB)
# 테스트 13 〉	통과 (0.01ms, 10MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.02ms, 10.2MB)
# 테스트 16 〉	통과 (0.02ms, 10.1MB)
# 테스트 17 〉	통과 (0.03ms, 10.1MB)
# 테스트 18 〉	통과 (0.02ms, 10MB)
# 테스트 19 〉	통과 (0.01ms, 10MB)
# 테스트 20 〉	통과 (0.01ms, 10.1MB)
# 테스트 21 〉	통과 (0.01ms, 10.1MB)
# 테스트 22 〉	통과 (0.02ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.1MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)
# 테스트 25 〉	통과 (0.01ms, 10MB)
    
# print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
# print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))


# 다른 사람 풀이 1
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]: # cards1의 길이가 0보다 크고 g가 card1[0]과 같으면
            cards1.pop(0)       # cards1의 제일 앞 요소를 뺀다. -> 그럼 계속 0번째 요소만 검사하면 된다.
        elif len(cards2) >0 and g == cards2[0]: # cards1과 같음
            cards2.pop(0)
        else:
            return "No" # 그리고 cards배열들의 원소가 남아있지 않거나 0번째 요소들이 같지 않다면 No를 반환한다.
    return "Yes" # 성공적으로 반복문을 돌면 Yes를 반환한다.
# 테스트 1 〉	통과 (0.00ms, 10MB)
# 테스트 2 〉	통과 (0.00ms, 10.1MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.00ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.00ms, 10.3MB)
# 테스트 9 〉	통과 (0.00ms, 10MB)
# 테스트 10 〉	통과 (0.00ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 9.99MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)
# 테스트 17 〉	통과 (0.01ms, 10.1MB)
# 테스트 18 〉	통과 (0.01ms, 10MB)
# 테스트 19 〉	통과 (0.01ms, 10.1MB)
# 테스트 20 〉	통과 (0.01ms, 10.1MB)
# 테스트 21 〉	통과 (0.00ms, 10.2MB)
# 테스트 22 〉	통과 (0.01ms, 10.1MB)
# 테스트 23 〉	통과 (0.01ms, 10.1MB)
# 테스트 24 〉	통과 (0.00ms, 10.1MB)
# 테스트 25 〉	통과 (0.01ms, 10.3MB)

  

# 다른 사람 풀이 2 -> 인덱스에 1씩 더해가면서 세는게 나랑 비슷한 것 같다...그런데 시간이 더 짧은..
def solution(cards1, cards2, goal):
    idx1,idx2=0,0
    for word in goal:
        if len(cards1)>idx1 and cards1[idx1]==word: # cards의 배열의 길이가 접근하려는 인덱스(idx1, idx2)보다 크고 word와 같으면  -> 배열의 길이보다 idx가 높아질 수 있으므로
            idx1+=1      # 인덱스를 올려준다. -> 인덱스를 1만 올렸기 때문에 바로 다음 요소인지 확인한다.
        elif len(cards2)>idx2 and cards2[idx2]==word:
            idx2+=1
        else:
            return "No"
    return "Yes"
# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.00ms, 10MB)
# 테스트 3 〉	통과 (0.00ms, 10.1MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.1MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.00ms, 10.1MB)
# 테스트 9 〉	통과 (0.00ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)
# 테스트 17 〉	통과 (0.01ms, 10.1MB)
# 테스트 18 〉	통과 (0.01ms, 10MB)
# 테스트 19 〉	통과 (0.00ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.4MB)
# 테스트 21 〉	통과 (0.00ms, 10.2MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.00ms, 10MB)
# 테스트 24 〉	통과 (0.00ms, 10.2MB)
# 테스트 25 〉	통과 (0.00ms, 10.1MB)

  
  
# 다른 사람 풀이 3
def solution(cards1, cards2, goal):
    answer = 'No'
    cards1_subset = []
    cards2_subset = []
    for w in goal:
        if w in cards1:
            cards1_subset.append(w) # goal을 반복문을 돌려서 같으면 배열에 추가하고
        elif w in cards2:
            cards2_subset.append(w)
    if cards1_subset == cards1[:len(cards1_subset)] and cards2_subset == cards2[:len(cards2_subset)]: # 추가한 subset배열과 원본 배열이 똑같을 때만 Yes를 반환한다.
        answer = 'Yes'

    return answer
# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.00ms, 10.1MB)
# 테스트 3 〉	통과 (0.00ms, 10.1MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.1MB)
# 테스트 7 〉	통과 (0.00ms, 10.1MB)
# 테스트 8 〉	통과 (0.00ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.1MB)
# 테스트 18 〉	통과 (0.01ms, 10.1MB)
# 테스트 19 〉	통과 (0.01ms, 10.3MB)
# 테스트 20 〉	통과 (0.01ms, 10.1MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 테스트 22 〉	통과 (0.01ms, 10MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (0.00ms, 10MB)
# 테스트 25 〉	통과 (0.01ms, 10.3MB)
