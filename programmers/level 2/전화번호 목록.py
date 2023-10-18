def solution(phone_book):
    answer = True
    target = min(phone_book, key = lambda n: len(n))
    t_len = len(target)
    hash_t = {}
    for i in range(len(phone_book)):
        hash_key = hash(phone_book[i][:t_len])
        if hash_key not in hash_t:
            hash_t[hash_key] = []
        hash_t[hash_key].append(phone_book[i])
    if len(hash_t[hash(target)]) > 1 :
      return False
    value_list = list(hash_t.values())
    for v in value_list:
        if 1 < len(v):
            short = min(v, key = lambda n: len(n))
            cnt = 0
            for item in v:
              if short in item:
                cnt += 1
                if cnt > 1:
                  return False
    return answer
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.02ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.68ms, 10.1MB)
# 테스트 15 〉	통과 (0.91ms, 10.4MB)
# 테스트 16 〉	통과 (1.95ms, 10.5MB)
# 테스트 17 〉	통과 (1.32ms, 10.6MB)
# 테스트 18 〉	통과 (2.83ms, 10.8MB)
# 테스트 19 〉	통과 (2.64ms, 10.9MB)
# 테스트 20 〉	통과 (2.01ms, 10.9MB)
# 효율성
# 테스트 1 〉	통과 (6.02ms, 10.9MB)
# 테스트 2 〉	통과 (4.14ms, 10.9MB)
# 테스트 3 〉	통과 (199.47ms, 70.7MB)
# 테스트 4 〉	통과 (137.95ms, 58.4MB)

# print(solution(["119", "97674223", "1195524421"])) # false
# print(solution(["123","456","789"])) # true
# print(solution(["12","123","1235","567","88"])) # false
# print(solution(["123", "1005", "1006", "1007"])) # true


# 다른 사람 풀이 1
# 정렬해서 풀 생각을 못했다!
# str.startswith(시작하는지 확인할 문자, 찾기 시작할 지점)
def solution(phoneBook):
    phoneBook = sorted(phoneBook) # 번호목록을 정렬한다.
    print(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]): # 정렬한 번호목록과 첫 요소를 제외한 정렬한 번호목록을 zip으로
        if p2.startswith(p1): # 비교해서 (0번째와 1번째, 1번째와 2번째) i+1번째가 i번째로 시작하는지 확인한다.
            return False # 그렇다면 False 리턴
    return True
# 테스트 1 〉	통과 (0.01ms, 10MB)
# 테스트 2 〉	통과 (0.00ms, 10MB)
# 테스트 3 〉	통과 (0.01ms, 9.99MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 9.94MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)
# 테스트 14 〉	통과 (0.49ms, 10.2MB)
# 테스트 15 〉	통과 (0.40ms, 10.4MB)
# 테스트 16 〉	통과 (0.69ms, 10.3MB)
# 테스트 17 〉	통과 (0.52ms, 10.1MB)
# 테스트 18 〉	통과 (0.76ms, 10.1MB)
# 테스트 19 〉	통과 (0.92ms, 10.2MB)
# 테스트 20 〉	통과 (0.99ms, 10.3MB)
# 효율성
# 테스트 1 〉	통과 (2.90ms, 10.9MB)
# 테스트 2 〉	통과 (2.95ms, 10.8MB)
# 테스트 3 〉	통과 (99.78ms, 30.7MB)
# 테스트 4 〉	통과 (88.71ms, 27.9MB)


# 다른 사람 풀이 2
# 해쉬를 사용한 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1 # hash_map에 key를 phone_number, value를 1로 담는다.
    for phone_number in phone_book: # phone_book을 다시 돌면서
        temp = ""
        for number in phone_number: # phone_number의 숫자를 하나씩 돌면서
            temp += number # temp에 추가해주고
            if temp in hash_map and temp != phone_number: # temp가 hash_map의 key면서 phone_number와 같지는 않을 때
                answer = False # 접두어라고 판단하여 False 리턴
    return answer
# 테스트 1 〉	통과 (0.01ms, 9.91MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.00ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 9.99MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10MB)
# 테스트 13 〉	통과 (0.00ms, 10.3MB)
# 테스트 14 〉	통과 (2.02ms, 10.2MB)
# 테스트 15 〉	통과 (2.09ms, 10.3MB)
# 테스트 16 〉	통과 (4.05ms, 10.4MB)
# 테스트 17 〉	통과 (4.56ms, 10.3MB)
# 테스트 18 〉	통과 (6.34ms, 10.3MB)
# 테스트 19 〉	통과 (6.55ms, 10.4MB)
# 테스트 20 〉	통과 (4.30ms, 10.5MB)
# 효율성
# 테스트 1 〉	통과 (21.70ms, 11.3MB)
# 테스트 2 〉	통과 (15.40ms, 11.3MB)
# 테스트 3 〉	통과 (887.60ms, 46.8MB)
# 테스트 4 〉	통과 (738.80ms, 34.5MB)