# 소수 찾기

# 소수 판별 알고리즘 
# 1부터 n까지 소수인지 판별한다. -> 시간이 너무 오래 걸림.

# 에라토스테네스의 체 -> worst case를 생각했을 때 제일 빠르다! (V)
# n의 수의 약수는 대칭을 이루는 성질을 활용해 n의 제곱근까지만 확인한다.

# 1. 2 ~ n까지 배열을 만든다.
# 2. 해당 배열 내의 가장 작은 수 i 부터 시작하여, i의 배수들을 해당 배열에서 지운다.
# 3. 주어진 범위 내에서 i의 배수가 모두 지워지면 i 다음으로 작은 수의 배수를 같은 방식으로 배열에서 지운다.
# 4. 더 이상 반복할 수 없을 때까지 위 과정을 반복한다.
import math

def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1

    return arr
  
def solution(n):
    count = 0
    for i in is_prime_num(n):
      if i == True:
        count += 1
    return count
  
# print(solution(10))
# print(solution(5))

# 다른 사람 풀이
def solution(n):
    num=set(range(2,n+1)) # 해당 숫자까지 집합을 만든다.

    for i in range(2,n+1): # 같은 범위로 반복문을 돌리는데
        if i in num: # 집합에 해당 수가 있으면
            num-=set(range(2*i,n+1,i)) # 해당 수의 2배가 되는 숫자부터 배수들을 집합에서 제거한다.
    return len(num) # 그리고 남은 집합의 길이 반환
  
# 다른 풀이들은 효율성 테스트 때문에 통과하지 못하는게 많은 것 같다.