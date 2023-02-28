# 가장 가까운 같은 글자

# 첫번째 풀이
def solution(s):
    answer = []
    char_obj = {}
    for char in s:
      if char in char_obj:
        prev_num = char_obj[char]
        now_num = list(s).index(char,char_obj[char]+1)
        char_obj[char] = now_num
        answer.append(now_num - prev_num)
      else:
        char_obj[char] = list(s).index(char)
        answer.append(-1)
    return answer
# 해야하는 연산 횟수가 많아서 시간이 너무 오래걸린다.
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.12ms, 10.2MB)
# 테스트 3 〉	통과 (0.21ms, 10.2MB)
# 테스트 4 〉	통과 (7.46ms, 10.2MB)
# 테스트 5 〉	통과 (736.58ms, 11MB)
# 테스트 6 〉	통과 (91.80ms, 10.2MB)
# 테스트 7 〉	통과 (476.24ms, 10.9MB)
# 테스트 8 〉	통과 (73.59ms, 10.3MB)
# 테스트 9 〉	통과 (661.54ms, 10.7MB)
# 테스트 10 〉	통과 (17.15ms, 10.4MB)
# 테스트 11 〉	통과 (481.47ms, 10.7MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)
# 테스트 14 〉	통과 (2.19ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.03ms, 10MB)
# 테스트 17 〉	통과 (0.09ms, 10.1MB)
# 테스트 18 〉	통과 (27.42ms, 10.2MB)
# 테스트 19 〉	통과 (41.33ms, 10.5MB)
# 테스트 20 〉	통과 (1.05ms, 10.1MB)
# 테스트 21 〉	통과 (0.15ms, 10.3MB)
# 테스트 22 〉	통과 (101.19ms, 10.2MB)
# 테스트 23 〉	통과 (1.00ms, 10.2MB)
# 테스트 24 〉	통과 (2.35ms, 10.2MB)
# 테스트 25 〉	통과 (2.95ms, 10.2MB)
# 테스트 26 〉	통과 (0.26ms, 10.1MB)
# 테스트 27 〉	통과 (5.09ms, 10.2MB)
# 테스트 28 〉	통과 (4.75ms, 10.1MB)
# 테스트 29 〉	통과 (0.00ms, 10.2MB)
# 테스트 30 〉	통과 (655.57ms, 10.9MB)
  

# 다른 사람 풀이 참고
def solution(s):
    answer = []
    char_obj = {}
    for i in range(len(s)):
      if s[i] in char_obj:
        answer.append(i-char_obj[s[i]])
      else:
        answer.append(-1)
      char_obj[s[i]] = i
    return answer
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.03ms, 10.1MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.35ms, 10.3MB)
# 테스트 5 〉	통과 (3.01ms, 10.8MB)
# 테스트 6 〉	통과 (0.90ms, 10.3MB)
# 테스트 7 〉	통과 (3.22ms, 11MB)
# 테스트 8 〉	통과 (1.02ms, 10.3MB)
# 테스트 9 〉	통과 (3.07ms, 10.7MB)
# 테스트 10 〉	통과 (0.34ms, 10.2MB)
# 테스트 11 〉	통과 (2.61ms, 10.7MB)
# 테스트 12 〉	통과 (0.01ms, 10MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.17ms, 10MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.02ms, 10.3MB)
# 테스트 18 〉	통과 (0.58ms, 10.3MB)
# 테스트 19 〉	통과 (0.38ms, 10.3MB)
# 테스트 20 〉	통과 (0.14ms, 10.1MB)
# 테스트 21 〉	통과 (0.03ms, 10.1MB)
# 테스트 22 〉	통과 (1.47ms, 10.3MB)
# 테스트 23 〉	통과 (0.13ms, 10.1MB)
# 테스트 24 〉	통과 (0.19ms, 10.4MB)
# 테스트 25 〉	통과 (0.20ms, 10.2MB)
# 테스트 26 〉	통과 (0.05ms, 10.2MB)
# 테스트 27 〉	통과 (0.24ms, 10.4MB)
# 테스트 28 〉	통과 (0.22ms, 10.1MB)
# 테스트 29 〉	통과 (0.01ms, 10.2MB)
# 테스트 30 〉	통과 (2.21ms, 10.9MB)

# print(solution('banana'))
# print(solution('foobar'))

# 다른 사람 풀이
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]]) # 복잡하게 생각할 것 없이 지금 인덱스에서 이전 인덱스를 뺐다.
        dic[s[i]] = i # 딕셔너리에 키&값을 추가. 가장 최근 알파벳의 인덱스를 무조건 저장함

    return answer
  
# 자꾸 반복문으로 range를 쓸 생각을 못한다. 파이썬도 숫자로 반복문 돌릴 수 있다는 걸 잊지말자...