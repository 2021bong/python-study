# 다른 사람 풀이 1
def prime(number):  # 소수인지 판단
    if number == 1:
        return False
    for i in range(2, int(number**(0.5))+1):  # 소수인지 판단하려는 수의 절반까지 보면 판단 가능
        if number % i == 0:  # number가 나누어 떨어지면 소수 아님
            return False
    return True  # 나누어 떨어지지 않으면 소수

def solution(n, k):
    num = []
    pb = ''
    while n != 0:
        # array.insert(array의 인덱스, 넣을 값)
        num.insert(0, n % k)  # n을 k로 나눈 나머지를 넣고
        n = n//k  # n을 k로 나눈 몫으로 n을 재할당

    for x in num:
        pb += str(x)  # num의 요소들을 붙여 pb에 n진법으로 변환한 수 할당

    spl = pb.split('0')  # pb를 0으로 나눔
    spl = [int(i) for i in spl if i != ""]  # spl의 빈 문자열이 아닌 요소들을 int로 변환
    answer = 0
    for x in spl:
        if prime(x):  # 소수인지 판단
            answer += 1  # 소수면 answer에 +1
    return answer


# print(solution(437674, 3))  # 3
# print(solution(110011, 10))  # 2


# 다른 사람 풀이 2
# n을 k진법으로 나타낸 문자열 반환
def conv(n, k):  # 진법 변환
    s = ''
    while n:
        s += str(n % k)  # 뒷자리부터 일단 추가하고
        n //= k
    return s[::-1]  # 리턴할때 뒤집기

# n이 소수인지 판정
def isprime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n: # n보다 i*i가 더 커지면 종료
        if n % i == 0:
            return False
        i += 1 # 2부터 숫자를 올려가며 판별
    return True

def solution(n, k):
    s = conv(n, k)
    cnt = 0
    for num in s.split('0'):
        if not num:
            continue  # 빈 문자열에 대한 예외처리 -> 빈 문자열을 제거하지 않고 반복문 돌림
        if isprime(int(num)):
            cnt += 1
    return cnt