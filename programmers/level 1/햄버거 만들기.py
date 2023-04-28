# 햄버거 만들기

def solution(ingredient):
    # ingredient = ''.join([str(i) for i in ingredient])
    answer = 0
    i = 0;
    while i < len(ingredient):
      if ingredient[i:i+4] == [1,2,3,1]:
            del (ingredient[i:i+4])         
            i = i-3                       
            answer += 1
      i += 1
      
    return answer
  
# print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
# print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
# print(solution([1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1])) # 3
# print(solution([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1])) # 3


# 다른 사람 풀이 1
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt
  

# 다른 사람 풀이 2 -> 내가 하고 싶던게 이거였는데 결국에는 다른 배열에 넣었어야 했구나..
def solution(ingredient):
    s = []
    answer = 0
    for i in ingredient:
        s.append(i)
        while s[-4:] == [1, 2, 3, 1]:
            s.pop()
            s.pop()
            s.pop()
            s.pop()
            answer += 1

    return answer
  
# 다들 스택으로 풀어야된다고, pop()이나 del()을 써야한다고 하는데 어떻게 하라는 건지를 몰랐다.....
# 배열에 넣어서 [-4:]로 보고 빼면 되는데.. 파이썬으로 풀면서... 나 이자식... 멍청....