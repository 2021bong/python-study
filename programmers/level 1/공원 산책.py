def solution(park, routes):
    start = []
    size_x = 0
    size_y = 0
    for i, y in enumerate(park):
      if "S" in y:
        start.append(i)
        start.append(y.find("S"))
        size_x = len(y)
        break
    size_y = len(park)

    for order in routes:
      direct, distance = order.split(' ')
      y, x = start[0], start[1]
      flag = True
      for i in range(int(distance)):
        if direct == "E":
          x += 1
          if x == size_x or x < 0 or park[y][x] == "X":
            flag = False
            break
        elif direct == "S":
          y += 1
          if y == size_y or y < 0 or park[y][x] == "X":
            flag = False
            break
        elif direct == "W":
          x -= 1
          if x == size_x or x < 0 or park[y][x] == "X":
            flag = False
            break
        elif direct == "N":
          y -= 1
          if y == size_y or y < 0 or park[y][x] == "X":
            flag = False
            break
      if flag:
        start[0], start[1] = y, x

    return start
# 테스트 1 〉	통과 (0.04ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.5MB)
# 테스트 3 〉	통과 (0.04ms, 10.5MB)
# 테스트 4 〉	통과 (0.11ms, 10.5MB)
# 테스트 5 〉	통과 (0.13ms, 10.5MB)
# 테스트 6 〉	통과 (0.16ms, 10.4MB)
# 테스트 7 〉	통과 (0.09ms, 10.5MB)
# 테스트 8 〉	통과 (0.12ms, 10.4MB)
# 테스트 9 〉	통과 (0.10ms, 10.4MB)
# 테스트 10 〉	통과 (0.14ms, 10.3MB)
# 테스트 11 〉	통과 (0.09ms, 10.5MB)
# 테스트 12 〉	통과 (0.15ms, 10.4MB)
# 테스트 13 〉	통과 (0.16ms, 10.3MB)
# 테스트 14 〉	통과 (0.16ms, 10.4MB)
# 테스트 15 〉	통과 (0.09ms, 10.5MB)
# 테스트 16 〉	통과 (0.05ms, 10.3MB)
# 테스트 17 〉	통과 (0.06ms, 10.4MB)
# 테스트 18 〉	통과 (0.04ms, 10.4MB)
# 테스트 19 〉	통과 (0.07ms, 10.4MB)
# 테스트 20 〉	통과 (0.03ms, 10.4MB)
# 좌표가 [세로, 가로] 였는데 [가로, 세로]를 반환하니.. 안풀렸던 것이다......

# print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])) # [2,1]
# print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])) # [0,1]
# print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])) # [0,0]


# 다른 사람 풀이 1
class Dog: # Dog 클래스 생성
    def __init__(self, x, y): # init
        self.x = x
        self.y = y
        self.g = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}

    def move(self, park, direction, distance):
        i, j = self.g[direction] # 방향에 따른 이동 칸수
        x, y = self.x + (i * distance), self.y + (j * distance) # 현재 위치에서 이동 칸수만큼 이동한 좌표
        if x < 0 or y < 0 or x >= len(park) or y >= len(park[0]): # 이동 후 공원을 벗어나는지 확인
            return park # 벗어나면 해당 경로 무효
        elif "X" in park[x][min(self.y, y) : max(self.y, y) + 1] or "X" in [
            row[y] for row in park[min(self.x, x) : max(self.x, x)]
        ]: # 이동하려는 경로에 X(장애물)가 있으면 => park[x][start:end], park[start:end]로 해당 명령으로 이동하는 위치를 다 가져와서 X가 있는지 판단
            return park # 해당 경로 무효
        park[self.x][self.y] = "O" # 시작점을
        park[x][y] = "S" # 변경한 좌표로 시작점으로 수정
        self.x = x # 현재 좌표 변경한 좌표로 수정
        self.y = y
        return park

    @classmethod
    def detect_start_dogs_location(self, park):
        for i, row in enumerate(park):
            for j, item in enumerate(row):
                if item == "S":
                    return i, j


def solution(park, routes):
    park = [list(row) for row in park]
    x, y = Dog.detect_start_dogs_location(park) # 시작 지점 찾기

    dog = Dog(x, y) # 시작 지점에 Dog 클래스 생성

    for route in routes: # 산책 경로를 하나씩 수행
        direction, distance = route.split()
        park = dog.move(park, direction, int(distance)) # 방향과 경로로 이동

    return [dog.x, dog.y]
# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.5MB)
# 테스트 3 〉	통과 (0.06ms, 10.3MB)
# 테스트 4 〉	통과 (0.10ms, 10.4MB)
# 테스트 5 〉	통과 (0.13ms, 10.4MB)
# 테스트 6 〉	통과 (0.23ms, 10.4MB)
# 테스트 7 〉	통과 (0.21ms, 10.3MB)
# 테스트 8 〉	통과 (0.20ms, 10.3MB)
# 테스트 9 〉	통과 (0.23ms, 10.4MB)
# 테스트 10 〉	통과 (0.18ms, 10.3MB)
# 테스트 11 〉	통과 (0.18ms, 10.3MB)
# 테스트 12 〉	통과 (0.45ms, 10.4MB)
# 테스트 13 〉	통과 (0.24ms, 10.3MB)
# 테스트 14 〉	통과 (0.19ms, 10.4MB)
# 테스트 15 〉	통과 (0.21ms, 10.4MB)
# 테스트 16 〉	통과 (0.10ms, 10.3MB)
# 테스트 17 〉	통과 (0.24ms, 10.4MB)
# 테스트 18 〉	통과 (0.08ms, 10.3MB)
# 테스트 19 〉	통과 (0.15ms, 10.4MB)
# 테스트 20 〉	통과 (0.13ms, 10.3MB)


# 다른 사람 풀이 2
def solution(park, routes):
    W = len(park[0])
    park = [['X']*(W+2)] + [[*'X'+i+'X'] for i in park] + [['X']*(W+2)] # 테두리를 장애물로 감쌈

    x,y = 1,0
    while park[x][y]!='S':
        y += 1
        if y>W:
            x,y = x+1,0

    delta = {k:v for k,v in zip('NEWS',[(-1,0),(0,1),(0,-1),(1,0)])}
    for i in routes:
        v,d = i.split()
        for k in range(1,int(d)+1):
            X,Y = x+k*delta[v][0], y+k*delta[v][1]
            if park[X][Y]=='X':
                break
        else:
            x,y = X,Y
    return [x-1,y-1]