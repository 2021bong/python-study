# 크기가 작은 부분 문자열

def solution(t, p):
  nums = []
  for i in range(len(t)):
    nums.append(t[i:len(p)+i])
  count = 0
  for n in nums:
    if len(n) == len(p) and int(n) <= int(p):
      count += 1
  return count

# 다른 사람 풀이
# 굳이 새 배열에 값을 돌면서 저장할 필요없이 자른 값을 바로바로 비교해서 count를 올린다.
def solution(t, p):
  count = 0
  for i in range(len(t) - len(p)+1): # p와 길이가 같은 마지막도 잘라줘야하기때문에 1을 더한다. -> '12345'와 '12'일때 '123','234','345'로 잘라야하면 '345'를 위해서 1을 더한다.
    if int(p) >= int(t[i:len(p)+i]):
      count += 1
  return count
  
# print(solution("3141592","271"))
# print(solution("500220839878","7"))
# print(solution("10203","15"))