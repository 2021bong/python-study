# 직사각형 넓이 구하기

def solution(dots):
    dots = sorted(dots)
    w = abs(dots[1][1] - dots[0][1])
    h = abs(dots[2][0] - dots[0][0])
    return w * h
  
# print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
# print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))