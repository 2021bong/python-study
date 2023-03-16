# 체육복

def solution(n, lost, reserve):
    can = 0
    double = set(lost) & set(reserve) # 다른 사람 풀이를 보고 나니 굳이 중복요소 수를 세서 더해줄게 아니라 중복요소를 제거하는게 더 나았을 것 같다.. 이것 때문에 틀리기도 했고..
    can = n - len(lost) + len(double)
    lost = list(set(lost) - set(double))
    reserve = list(set(reserve) - set(double))
    for i in lost:
      if i - 1 in reserve:
        can += 1
        reserve.remove(i-1)
      elif i + 1 in reserve:
        can += 1
        reserve.remove(i+1)
      else:
        continue
    return can

# 이렇게 풀이하면 60/100이 나온다.
def solution(n, lost, reserve):
    can = 0
    double = set(lost) & set(reserve)
    if len(double) == 0:
      can = n - len(lost)
    else :
      can = n - len(lost) + 1 # 왜냐면 중복되는 원소가 여러 개 일 수도 있기 때문에...!!!!!!! ㅠㅠ 이걸로 40분 고민했다.. 왜 이런 짓을....
      lost = list(set(lost) - set(double))
      reserve = list(set(reserve) - set(double))
    for i in lost:
      if i - 1 in reserve:
        can += 1
        reserve.remove(i-1)
      elif i + 1 in reserve:
        can += 1
        reserve.remove(i+1)
      else:
        continue
    return can
  
# print(solution(5, [2,4], [1,3,5]))
# print(solution(5, [2,4], [3]))
# print(solution(3, [3], [1]))
# print(solution(5, [1,3], [2,3])) # 5
# print(solution(5, [4,1], [2,3])) # 5
# print(solution(5, [1,3], [5])) # 3
# print(solution(30, [1,3], [3,5])) # 29
# print(solution(8, [5, 6, 7, 8], [4, 7])) # 6
  
  
  
# 다를 사람 풀이 1
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost] # 한줄 반복문으로 반복 요소 제거
    _lost = [l for l in lost if l not in reserve] # 애초에 중복 요소를 제거하고 시작한다.
    for r in _reserve:
        f = r - 1 # 앞번호
        b = r + 1 # 뒷번호
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost) # 중복 요소를 없앴기 때문에 위에서 _lost에 남아있는 학생만 체육복을 못빌린 것이므로 전체에서 뺀다.
  
  
# 다른 사람 풀이 2
def solution(n, lost, reserve):
    reserved = 0
    lostN = list(set(lost) - set(reserve))
    reserveN = list(set(reserve) - set(lost))
    lostN.sort() # 힌트에서 정렬에 대한 이야기가 나왔는데
    for l in lostN:
        for x in range(l-1, l+2): # 반복문을 이런식으로 돌려야하면 그럴수도 있겠다.
            if x in reserveN:
                reserveN.remove(x)
                reserved += 1
                break
    return n - len(lostN) + reserved