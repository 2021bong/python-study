# 캐릭터의 좌표

# 파이썬은 switch문이 없다. 도입하려는 시도는 있었으나 사람들이 크게 관심을 가지지 않아 도입하지 않았다.
# switch문 대신 if - elif나 dictionary 사용을 권장한다.

# 첫번째 풀이
# def checkSize(answer, board, xy):
#     if abs(answer[xy]) > (board[xy]-1) / 2:
#       if answer[xy] > 0:
#         answer[xy] = int((board[xy]-1) / 2)
#       else:
#         answer[xy] = int(((board[xy]-1) / 2)) * -1

# def solution(keyinput, board):
#   answer = [0,0]
#   for dir in keyinput:
#     if dir == 'left':
#       answer[0] += -1
#       checkSize(answer, board, 0)
#     elif dir == 'right':
#       answer[0] += 1
#       checkSize(answer, board, 0)
#     elif dir == 'up':  
#       answer[1] += 1
#       checkSize(answer, board, 1)
#     elif dir == 'down':  
#       answer[1] += -1
#       checkSize(answer, board, 1)
#     else:
#       continue
      
#   return answer

# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.4MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)

def checkSize(answer, board, xy):
    if answer[xy] > 0:
      answer[xy] = int((board[xy]-1) / 2)
    else:
      answer[xy] = int(((board[xy]-1) / 2)) * -1

def solution(keyinput, board):
  answer = [0,0]
  x, y = (board[0]-1) / 2, (board[1]-1) / 2
  for dir in keyinput:
    if dir == 'left':
      answer[0] += -1
      if abs(answer[0]) > x:
        checkSize(answer, board, 0)
    elif dir == 'right':
      answer[0] += 1
      if abs(answer[0]) > x:
        checkSize(answer, board, 0)
    elif dir == 'up':  
      answer[1] += 1
      if abs(answer[1]) > y:
        checkSize(answer, board, 1)
    elif dir == 'down':  
      answer[1] += -1
      if abs(answer[1]) > y:
        checkSize(answer, board, 1)
    else:
      continue
      
  return answer

# if문으로 선택적으로 함수를 실행하게 하는게 시간이 더 짧아서 수정함
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.4MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.4MB)
# 테스트 10 〉	통과 (0.00ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
  
# print(solution(["left", "right", "up", "right", "right"],[11, 11]))
# print(solution(["down", "down", "down", "down", "down"], [7, 9]))
# print(solution(["down", "down", "up", "up", "up"],[3, 3]))
# print(solution(["down", "down", "down", "up"], [3, 3]))