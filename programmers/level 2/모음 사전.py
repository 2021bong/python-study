# 다른 사람 풀이 0
# 그냥 모든 조합을 순서대로 냅다 list에 넣고 인덱스를 찾음. 시간도 빠름ㅋㅋㅋ 이 정도 열정은 있어줘야 되는데.. 반성합니다...
# 테스트 1 〉	통과 (0.03ms, 13.7MB)
# 테스트 2 〉	통과 (0.03ms, 13.8MB)
# 테스트 3 〉	통과 (0.08ms, 13.7MB)
# 테스트 4 〉	통과 (0.10ms, 13.7MB)
# 테스트 5 〉	통과 (0.08ms, 13.6MB)
# 테스트 6 〉	통과 (0.03ms, 13.8MB)
# 테스트 7 〉	통과 (0.07ms, 13.9MB)
# 테스트 8 〉	통과 (0.04ms, 13.8MB)
# 테스트 9 〉	통과 (0.04ms, 13.7MB)
# 테스트 10 〉	통과 (0.03ms, 13.8MB)
# 테스트 11 〉	통과 (0.06ms, 13.6MB)
# 테스트 12 〉	통과 (0.03ms, 13.9MB)
# 테스트 13 〉	통과 (0.05ms, 13.8MB)
# 테스트 14 〉	통과 (0.05ms, 13.8MB)
# 테스트 15 〉	통과 (0.06ms, 13.7MB)
# 테스트 16 〉	통과 (0.05ms, 13.9MB)
# 테스트 17 〉	통과 (0.13ms, 13.6MB)
# 테스트 18 〉	통과 (0.05ms, 13.7MB)
# 테스트 19 〉	통과 (0.08ms, 13.8MB)
# 테스트 20 〉	통과 (0.03ms, 13.8MB)
# 테스트 21 〉	통과 (0.04ms, 13.8MB)
# 테스트 22 〉	통과 (0.07ms, 13.8MB)
# 테스트 23 〉	통과 (0.03ms, 13.8MB)
# 테스트 24 〉	통과 (0.03ms, 13.8MB)
# 테스트 25 〉	통과 (0.03ms, 13.8MB)
# 테스트 26 〉	통과 (0.04ms, 13.9MB)
# 테스트 27 〉	통과 (0.06ms, 13.7MB)
# 테스트 28 〉	통과 (0.09ms, 13.8MB)
# 테스트 29 〉	통과 (0.02ms, 13.8MB)
# 테스트 30 〉	통과 (0.03ms, 13.9MB)
# 테스트 31 〉	통과 (0.06ms, 13.8MB)
# 테스트 32 〉	통과 (0.05ms, 13.9MB)
# 테스트 33 〉	통과 (0.16ms, 13.7MB)
# 테스트 34 〉	통과 (0.05ms, 13.8MB)
# 테스트 35 〉	통과 (0.12ms, 13.6MB)
# 테스트 36 〉	통과 (0.06ms, 13.7MB)
# 테스트 37 〉	통과 (0.05ms, 13.8MB)
# 테스트 38 〉	통과 (0.06ms, 13.8MB)
# 테스트 39 〉	통과 (0.05ms, 13.9MB)
# 테스트 40 〉	통과 (0.04ms, 13.8MB)

# 다른 사람 풀이 1
# 손수 구현을 못하겠으면 모듈이라도 썼어야됐는데 그런 모듈이 있다는 사실을 까먹음.......... 
from itertools import product

def solution(word):
    # 만들 수 있는 단어 중복 순열로 생성
    lis = list()
    words = ['A','E','I','O','U']
    for j in range(1,6):
        for i in product(words,repeat=j): # 1부터 5까지 중복 가능하도록 하여
            lis.append(list(i)) # lis에 추가 -> 모든 가능한 단어가 추가됨
    lis.sort() # lis 정렬
    # word와 단어 비교
    answer = 0
    for i in lis : # 사전의 맨 앞부터 탐색
        answer += 1 # 인덱스
        st = ''.join(s for s in i) # i만 넣어도 되지않나..?
        if (st == word): # 단어와 같으면 멈춤
            break
    return answer
# 테스트 1 〉	통과 (2.58ms, 10.2MB)
# 테스트 2 〉	통과 (1.57ms, 10.2MB)
# 테스트 3 〉	통과 (3.24ms, 10.2MB)
# 테스트 4 〉	통과 (5.59ms, 10.3MB)
# 테스트 5 〉	통과 (5.62ms, 10.2MB)
# 테스트 6 〉	통과 (1.95ms, 10.3MB)
# 테스트 7 〉	통과 (3.57ms, 10.3MB)
# 테스트 8 〉	통과 (3.81ms, 10.2MB)
# 테스트 9 〉	통과 (4.41ms, 10.3MB)
# 테스트 10 〉	통과 (1.88ms, 10.2MB)
# 테스트 11 〉	통과 (3.14ms, 10.2MB)
# 테스트 12 〉	통과 (3.22ms, 10.3MB)
# 테스트 13 〉	통과 (2.69ms, 10.2MB)
# 테스트 14 〉	통과 (5.30ms, 10.2MB)
# 테스트 15 〉	통과 (6.20ms, 10.2MB)
# 테스트 16 〉	통과 (2.74ms, 10.4MB)
# 테스트 17 〉	통과 (3.25ms, 10.2MB)
# 테스트 18 〉	통과 (2.05ms, 10.3MB)
# 테스트 19 〉	통과 (5.84ms, 10.3MB)
# 테스트 20 〉	통과 (1.87ms, 10.2MB)
# 테스트 21 〉	통과 (2.69ms, 10.2MB)
# 테스트 22 〉	통과 (3.00ms, 10.2MB)
# 테스트 23 〉	통과 (2.80ms, 10.3MB)
# 테스트 24 〉	통과 (3.48ms, 10.2MB)
# 테스트 25 〉	통과 (2.68ms, 10.2MB)
# 테스트 26 〉	통과 (2.01ms, 10.2MB)
# 테스트 27 〉	통과 (5.07ms, 10.2MB)
# 테스트 28 〉	통과 (3.59ms, 10.4MB)
# 테스트 29 〉	통과 (1.40ms, 10.2MB)
# 테스트 30 〉	통과 (2.91ms, 10.2MB)
# 테스트 31 〉	통과 (2.49ms, 10.2MB)
# 테스트 32 〉	통과 (2.69ms, 10.4MB)
# 테스트 33 〉	통과 (4.15ms, 10.2MB)
# 테스트 34 〉	통과 (3.30ms, 10.1MB)
# 테스트 35 〉	통과 (3.49ms, 10.4MB)
# 테스트 36 〉	통과 (3.57ms, 10.2MB)
# 테스트 37 〉	통과 (2.21ms, 10.2MB)
# 테스트 38 〉	통과 (2.62ms, 10.2MB)
# 테스트 39 〉	통과 (2.43ms, 10.3MB)
# 테스트 40 〉	통과 (1.93ms, 10.3MB)

# 다른 사람 풀이 2
from itertools import product

solution = lambda word: sorted([
  "".join(c) # 3. 한걸 문자열로 바꿔서
  for i in range(5) # 1. 중복 1부터 5까지
  for c in product("AEIOU", repeat=i+1) # 2. 조합 생성
  ]) # 4. 정렬한 배열
.index(word) + 1 # 5. 의 word의 인덱스 + 1
# 테스트 1 〉	통과 (0.83ms, 10.2MB)
# 테스트 2 〉	통과 (0.82ms, 10.3MB)
# 테스트 3 〉	통과 (1.35ms, 10.4MB)
# 테스트 4 〉	통과 (0.86ms, 10.2MB)
# 테스트 5 〉	통과 (1.46ms, 10.1MB)
# 테스트 6 〉	통과 (1.06ms, 10.3MB)
# 테스트 7 〉	통과 (1.38ms, 10.2MB)
# 테스트 8 〉	통과 (1.35ms, 10.1MB)
# 테스트 9 〉	통과 (0.99ms, 10.3MB)
# 테스트 10 〉	통과 (1.25ms, 10.2MB)
# 테스트 11 〉	통과 (0.83ms, 10.3MB)
# 테스트 12 〉	통과 (0.80ms, 10.2MB)
# 테스트 13 〉	통과 (1.40ms, 10.3MB)
# 테스트 14 〉	통과 (1.49ms, 10.4MB)
# 테스트 15 〉	통과 (1.13ms, 10.2MB)
# 테스트 16 〉	통과 (1.57ms, 10.2MB)
# 테스트 17 〉	통과 (0.86ms, 10.3MB)
# 테스트 18 〉	통과 (0.80ms, 10.4MB)
# 테스트 19 〉	통과 (0.85ms, 10.3MB)
# 테스트 20 〉	통과 (1.56ms, 10.2MB)
# 테스트 21 〉	통과 (0.82ms, 10.3MB)
# 테스트 22 〉	통과 (0.81ms, 10.3MB)
# 테스트 23 〉	통과 (1.04ms, 10.3MB)
# 테스트 24 〉	통과 (1.34ms, 10.3MB)
# 테스트 25 〉	통과 (0.77ms, 10.1MB)
# 테스트 26 〉	통과 (0.80ms, 10.2MB)
# 테스트 27 〉	통과 (0.82ms, 10.2MB)
# 테스트 28 〉	통과 (0.84ms, 10.3MB)
# 테스트 29 〉	통과 (1.55ms, 10.2MB)
# 테스트 30 〉	통과 (1.55ms, 10.3MB)
# 테스트 31 〉	통과 (0.77ms, 10.3MB)
# 테스트 32 〉	통과 (0.84ms, 10.2MB)
# 테스트 33 〉	통과 (0.91ms, 10.3MB)
# 테스트 34 〉	통과 (1.53ms, 10.1MB)
# 테스트 35 〉	통과 (1.58ms, 10.1MB)
# 테스트 36 〉	통과 (0.83ms, 10.3MB)
# 테스트 37 〉	통과 (1.04ms, 10.2MB)
# 테스트 38 〉	통과 (0.80ms, 10.3MB)
# 테스트 39 〉	통과 (0.77ms, 10.2MB)
# 테스트 40 〉	통과 (0.83ms, 10.2MB)

# 다른 사람 풀이 3
# https://pinopino.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AA%A8%EC%9D%8C-%EC%82%AC%EC%A0%84
def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)
# 테스트 17 〉	통과 (0.01ms, 10.1MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 테스트 19 〉	통과 (0.01ms, 10MB)
# 테스트 20 〉	통과 (0.02ms, 10MB)
# 테스트 21 〉	통과 (0.01ms, 10MB)
# 테스트 22 〉	통과 (0.01ms, 10MB)
# 테스트 23 〉	통과 (0.01ms, 10.1MB)
# 테스트 24 〉	통과 (0.01ms, 10.3MB)
# 테스트 25 〉	통과 (0.01ms, 10.1MB)
# 테스트 26 〉	통과 (0.01ms, 10.1MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)
# 테스트 28 〉	통과 (0.01ms, 10MB)
# 테스트 29 〉	통과 (0.01ms, 10MB)
# 테스트 30 〉	통과 (0.01ms, 10MB)
# 테스트 31 〉	통과 (0.01ms, 10.2MB)
# 테스트 32 〉	통과 (0.01ms, 10MB)
# 테스트 33 〉	통과 (0.01ms, 10.1MB)
# 테스트 34 〉	통과 (0.01ms, 10.1MB)
# 테스트 35 〉	통과 (0.01ms, 10.1MB)
# 테스트 36 〉	통과 (0.01ms, 10.1MB)
# 테스트 37 〉	통과 (0.01ms, 10.1MB)
# 테스트 38 〉	통과 (0.01ms, 10.1MB)
# 테스트 39 〉	통과 (0.01ms, 10.1MB)
# 테스트 40 〉	통과 (0.01ms, 9.95MB)

# 다른 사람 풀이 4
# 처음에 이렇게 풀고 싶었는데 원하던데로 안돼서 포기..
def solution(word):
    answer = 0
    alpha  = ["A","E","I","O","U",""]
    ans = []
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for l in alpha:
                    for m in alpha:
                        w = i+j+k+l+m # 5단 반복문으로 조합해서 생성
                        if w not in ans: ans.append(w) # 중복 체크 해서 없을 때만 넣음
    ans.sort() # 정렬
    answer = ans.index(word) # 인덱스 찾기
    return answer
# 테스트 1 〉	통과 (223.16ms, 10.2MB)
# 테스트 2 〉	통과 (246.93ms, 10.1MB)
# 테스트 3 〉	통과 (255.29ms, 10.2MB)
# 테스트 4 〉	통과 (281.14ms, 10.2MB)
# 테스트 5 〉	통과 (225.46ms, 10.2MB)
# 테스트 6 〉	통과 (207.79ms, 10.3MB)
# 테스트 7 〉	통과 (288.00ms, 10.1MB)
# 테스트 8 〉	통과 (264.51ms, 10.1MB)
# 테스트 9 〉	통과 (307.19ms, 10.2MB)
# 테스트 10 〉	통과 (235.10ms, 10.2MB)
# 테스트 11 〉	통과 (212.40ms, 10.4MB)
# 테스트 12 〉	통과 (221.01ms, 10.2MB)
# 테스트 13 〉	통과 (229.60ms, 10.2MB)
# 테스트 14 〉	통과 (299.84ms, 10.1MB)
# 테스트 15 〉	통과 (268.43ms, 10.3MB)
# 테스트 16 〉	통과 (218.77ms, 10.3MB)
# 테스트 17 〉	통과 (207.21ms, 10.3MB)
# 테스트 18 〉	통과 (206.58ms, 10.2MB)
# 테스트 19 〉	통과 (219.37ms, 10.2MB)
# 테스트 20 〉	통과 (219.67ms, 10.2MB)
# 테스트 21 〉	통과 (207.41ms, 10.4MB)
# 테스트 22 〉	통과 (207.19ms, 10.4MB)
# 테스트 23 〉	통과 (219.45ms, 10.1MB)
# 테스트 24 〉	통과 (219.39ms, 10.2MB)
# 테스트 25 〉	통과 (206.57ms, 10.2MB)
# 테스트 26 〉	통과 (207.26ms, 10.4MB)
# 테스트 27 〉	통과 (207.40ms, 10.3MB)
# 테스트 28 〉	통과 (218.95ms, 10.1MB)
# 테스트 29 〉	통과 (218.75ms, 10.1MB)
# 테스트 30 〉	통과 (219.27ms, 10.2MB)
# 테스트 31 〉	통과 (206.67ms, 10.3MB)
# 테스트 32 〉	통과 (206.76ms, 10.2MB)
# 테스트 33 〉	통과 (210.38ms, 10.2MB)
# 테스트 34 〉	통과 (245.41ms, 10.2MB)
# 테스트 35 〉	통과 (218.67ms, 10.2MB)
# 테스트 36 〉	통과 (219.42ms, 10.1MB)
# 테스트 37 〉	통과 (244.87ms, 10.2MB)
# 테스트 38 〉	통과 (248.46ms, 10.3MB)
# 테스트 39 〉	통과 (206.53ms, 10.3MB)
# 테스트 40 〉	통과 (223.06ms, 10.2MB)
  
# 다른 사람 풀이 5
# 2번째로 이렇게 생각도 했는데 어떻게 구해야할지 몰라서 포기..
def solution(word):
    preset = dict()
    preset['A'] = [1,1,1,1,1]
    preset['E'] = [782,157,32,7,2]
    preset['I'] = [1563,313,63,13,3]
    preset['O'] = [2344,469,94,19,4]
    preset['U'] = [3125,625,125,25,5]
    ######### 사전이므로 idx4부터 따라올라가면
    ########## preset 산출가능함

    ans=0
    for idx, key in enumerate(word):
        ans+=preset[key][idx] # 글자의 인덱스를 더해서 구함
    return ans
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.00ms, 10.1MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.3MB)
# 테스트 8 〉	통과 (0.00ms, 10.2MB)
# 테스트 9 〉	통과 (0.00ms, 9.99MB)
# 테스트 10 〉	통과 (0.00ms, 10.2MB)
# 테스트 11 〉	통과 (0.00ms, 10.3MB)
# 테스트 12 〉	통과 (0.00ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.00ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.00ms, 10.1MB)
# 테스트 18 〉	통과 (0.00ms, 10.1MB)
# 테스트 19 〉	통과 (0.00ms, 10.2MB)
# 테스트 20 〉	통과 (0.00ms, 10.1MB)
# 테스트 21 〉	통과 (0.00ms, 10.1MB)
# 테스트 22 〉	통과 (0.00ms, 10.3MB)
# 테스트 23 〉	통과 (0.00ms, 10MB)
# 테스트 24 〉	통과 (0.00ms, 10.3MB)
# 테스트 25 〉	통과 (0.00ms, 9.98MB)
# 테스트 26 〉	통과 (0.01ms, 10.2MB)
# 테스트 27 〉	통과 (0.00ms, 10.1MB)
# 테스트 28 〉	통과 (0.00ms, 10.3MB)
# 테스트 29 〉	통과 (0.01ms, 10.1MB)
# 테스트 30 〉	통과 (0.00ms, 10.3MB)
# 테스트 31 〉	통과 (0.00ms, 10.2MB)
# 테스트 32 〉	통과 (0.00ms, 10.3MB)
# 테스트 33 〉	통과 (0.00ms, 10.2MB)
# 테스트 34 〉	통과 (0.00ms, 10.1MB)
# 테스트 35 〉	통과 (0.00ms, 10.1MB)
# 테스트 36 〉	통과 (0.00ms, 10.1MB)
# 테스트 37 〉	통과 (0.00ms, 10.1MB)
# 테스트 38 〉	통과 (0.00ms, 10.1MB)
# 테스트 39 〉	통과 (0.00ms, 10.1MB)
# 테스트 40 〉	통과 (0.00ms, 10.2MB)

# print(solution('AAAAE')) # 6
# print(solution('AAAE')) # 10
# print(solution('I')) # 1563
# print(solution('EIO')) # 1189
