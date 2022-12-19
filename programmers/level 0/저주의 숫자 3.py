# 저주의 숫자 3

def solution(n):
    arrOfAll = []
    for i in range(1, 187):
      if i % 3 != 0 and '3' not in str(i):
        arrOfAll.append(i)
    
    return arrOfAll[n - 1]
  
print(solution(15))
print(solution(40))