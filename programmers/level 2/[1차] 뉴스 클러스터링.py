def solution(str1, str2):  # 65536를 곱하여 정수부만
    str1_multiset = []
    str2_multiset = []
    for i in range(len(str1)):
        two_str = str1[i:i+2].strip().lower()
        if len(two_str) == 2 and 97 <= ord(two_str[0]) and 122 >= ord(two_str[0]) and 97 <= ord(two_str[1]) and 122 >= ord(two_str[1]):
            str1_multiset.append(two_str)
    for i in range(len(str2)):
        two_str = str2[i:i+2].strip().lower()
        if len(two_str) == 2 and 97 <= ord(two_str[0]) and 122 >= ord(two_str[0]) and 97 <= ord(two_str[1]) and 122 >= ord(two_str[1]):
            str2_multiset.append(two_str)
    if len(str1_multiset) == 0 and len(str2_multiset) == 0:
        return 65536
    intersection = str1_multiset.copy()
    temp = str1_multiset.copy()
    union = []
    for str in str2_multiset:
        if str not in temp:
            intersection.append(str)
        else:
            temp.remove(str)
    for str in str2_multiset:
        if str in str1_multiset:
            str1_multiset.remove(str)
            union.append(str)
    return int(len(union) / len(intersection) * 65536)
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (1.47ms, 10.1MB)
# 테스트 5 〉	통과 (0.04ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.24ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
# 테스트 9 〉	통과 (0.12ms, 10.2MB)
# 테스트 10 〉	통과 (0.29ms, 10.1MB)
# 테스트 11 〉	통과 (0.46ms, 10.4MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.07ms, 10.4MB)

# print(solution('FRANCE', 'french'))  # 16384
# print(solution('handshake', 'shake hands'))  # 65536
# print(solution('aa1+aa2', 'AAAA12'))  # 43690
# print(solution('E=M*C^2', 'e=m*c^2'))  # 65536


# 다른 사람 풀이 1
# str.count('str') : 해당 문자열이 몇번 들어가있는지를 센다.
# re.findall('정규식', 'str') : 정규식 함수
import math
import re

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])] # 2글자씩 끊어서 배열 생성
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)  # 교집합
    hap = set(str1) | set(str2)  # 합집합
    print(gyo, hap)
    if len(hap) == 0:
        return 65536

    # 집합으로 중복제거한 요소들로 for문을 돌려서 원본 문자열에 몇번 들어가나 센 다음
    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])  # 제일 작은 개수들의 합 - 교집합 개수
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])  # 제일 큰 개수들의 합 - 합집합 개수
    return math.floor((gyo_sum/hap_sum)*65536)
# 테스트 1 〉	통과 (0.11ms, 10.3MB)
# 테스트 2 〉	통과 (0.12ms, 10.2MB)
# 테스트 3 〉	통과 (0.10ms, 10.3MB)
# 테스트 4 〉	통과 (10.26ms, 10.3MB)
# 테스트 5 〉	통과 (0.14ms, 10.2MB)
# 테스트 6 〉	통과 (0.16ms, 10.2MB)
# 테스트 7 〉	통과 (0.42ms, 10.2MB)
# 테스트 8 〉	통과 (0.11ms, 10.4MB)
# 테스트 9 〉	통과 (0.36ms, 10.2MB)
# 테스트 10 〉	통과 (0.74ms, 10.3MB)
# 테스트 11 〉	통과 (1.46ms, 10.2MB)
# 테스트 12 〉	통과 (0.10ms, 10.4MB)
# 테스트 13 〉	통과 (0.22ms, 10.2MB)


# 다른 사람 풀이 2
# str.isalpha() : 알파벳 or 한글인지 확인 (숫자, 공백, 특수문자가 들어가면 False를 반환)
# collections.Counter() : 인자로 넘기면 몇 번씩 나타나는지를 알려줌 -> 정말 신기하다 알아서 구해주고 집합 연산도 할 수 있음
# Counter("hello world") -> Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
from collections import Counter
def solution(str1, str2):
    # make sets
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()] # 2글자씩 끊어서 배열 생성
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1 and not s2:
        return 65536
    # 해당 배열로 Count 객체 생성 
    c1 = Counter(s1) # Counter({'fr': 1, 'ra': 1, 'an': 1, 'nc': 1, 'ce': 1})
    c2 = Counter(s2) # Counter({'fr': 1, 're': 1, 'en': 1, 'nc': 1, 'ch': 1})
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536) # Count 객체로 합집합, 교집합을 구하고 요소의 values()를 합함
    return answer
# 테스트 1 〉	통과 (0.06ms, 10.2MB)
# 테스트 2 〉	통과 (0.06ms, 10.1MB)
# 테스트 3 〉	통과 (0.05ms, 10.2MB)
# 테스트 4 〉	통과 (0.83ms, 10.5MB)
# 테스트 5 〉	통과 (0.05ms, 10.1MB)
# 테스트 6 〉	통과 (0.06ms, 10.3MB)
# 테스트 7 〉	통과 (0.12ms, 10.3MB)
# 테스트 8 〉	통과 (0.05ms, 10.4MB)
# 테스트 9 〉	통과 (0.16ms, 10.3MB)
# 테스트 10 〉	통과 (0.16ms, 10.2MB)
# 테스트 11 〉	통과 (0.24ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.09ms, 10.4MB)

# print(solution('FRANCE', 'french'))  # 16384
