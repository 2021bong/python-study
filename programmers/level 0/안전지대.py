# 안전지대

# 2차원 리스트를 1차원 리스트로 만들기
# sum(2차원 리스트, [])

# lambda
# filter(lambda 변수 : 변수를 이용한 조건, filter를 돌릴 리스트)
# filter(lambda num: num == 0 ,ans)
# filter 함수는 filter타입 결과를 반환해서 list로 형변환 해주어야함

def solution(board):
    bomb = [];
    for i, value in enumerate(board):
      for j, value2 in enumerate(board):
        if board[i][j] == 1:
          bomb.append([i, j])
    if len(bomb) / len(board) == len(board):
      return 0
    for i, value in enumerate(bomb):
      if bomb[i][0] == 0 and bomb[i][1] == 0:
        board[bomb[i][0]][bomb[i][1] + 1] = 1
        board[bomb[i][0] + 1][bomb[i][1]] = 1
        board[bomb[i][0] + 1][bomb[i][1] + 1] = 1
      elif bomb[i][0] == 0 and bomb[i][1] == len(board) - 1:
        board[bomb[i][0]][bomb[i][1] - 1] = 1
        board[bomb[i][0] + 1][bomb[i][1] - 1] = 1
        board[bomb[i][0] + 1][bomb[i][1]] = 1
      elif bomb[i][0] == len(board) - 1 and bomb[i][1] == len(board) - 1:
        board[bomb[i][0] - 1][bomb[i][1] - 1] = 1
        board[bomb[i][0] - 1][bomb[i][1]] = 1
        board[bomb[i][0]][bomb[i][1] - 1] = 1
      elif bomb[i][0] == len(board) - 1 and bomb[i][1] == 0:
        board[bomb[i][0] - 1][bomb[i][1]] = 1
        board[bomb[i][0] - 1][bomb[i][1] + 1] = 1
        board[bomb[i][0]][bomb[i][1] + 1] = 1
      elif bomb[i][0] == 0:
        board[bomb[i][0]][bomb[i][1] - 1] = 1
        board[bomb[i][0]][bomb[i][1] + 1] = 1
        board[bomb[i][0] + 1][bomb[i][1] - 1] = 1
        board[bomb[i][0] + 1][bomb[i][1]] = 1
        board[bomb[i][0] + 1][bomb[i][1] + 1] = 1
      elif bomb[i][0] == len(board) - 1:
        board[bomb[i][0] - 1][bomb[i][1] - 1] = 1
        board[bomb[i][0] - 1][bomb[i][1]] = 1
        board[bomb[i][0] - 1][bomb[i][1] + 1] = 1
        board[bomb[i][0]][bomb[i][1] + 1] = 1
        board[bomb[i][0]][bomb[i][1] - 1] = 1
      elif bomb[i][1] == 0:
        board[bomb[i][0] - 1][bomb[i][1]] = 1
        board[bomb[i][0] - 1][bomb[i][1] + 1] = 1
        board[bomb[i][0]][bomb[i][1] + 1] = 1
        board[bomb[i][0] + 1][bomb[i][1]] = 1
        board[bomb[i][0] + 1][bomb[i][1] + 1] = 1
      elif bomb[i][1] == len(board) - 1:
        board[bomb[i][0] - 1][bomb[i][1] - 1] = 1
        board[bomb[i][0] - 1][bomb[i][1]] = 1
        board[bomb[i][0]][bomb[i][1] - 1] = 1
        board[bomb[i][0] + 1][bomb[i][1] - 1] = 1
        board[bomb[i][0] + 1][bomb[i][1]] = 1
      else :
        board[bomb[i][0] - 1][bomb[i][1] - 1] = 1
        board[bomb[i][0] - 1][bomb[i][1]] = 1
        board[bomb[i][0] - 1][bomb[i][1] + 1] = 1
        board[bomb[i][0]][bomb[i][1] - 1] = 1
        board[bomb[i][0]][bomb[i][1] + 1] = 1
        board[bomb[i][0] + 1][bomb[i][1] - 1] = 1
        board[bomb[i][0] + 1][bomb[i][1]] = 1
        board[bomb[i][0] + 1][bomb[i][1] + 1] = 1
        
    ans = sum(board, []);
        
    return len(list(filter(lambda num: num == 0 ,ans)))

case1 = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
];
case2 = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0],
];
case3 = [
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
];

print(solution(case1))
print(solution(case2))


# JS 풀이 (추접스럽게 풀었지만.. 어쩔 수 없었음...)

# function solution(board) {
#   const safeboard = board.map((el) => el.map((el) => el));
#   const bomb = [];
#   for (let i = 0; i < board.length; i += 1) {
#     for (let j = 0; j < board.length; j += 1) {
#       if (board[i][j] === 1) {
#         bomb.push([i, j]);
#       }
#     }
#   }
#   if (bomb.length / board.length === board.length) return 0;
#   for (let i = 0; i < bomb.length; i += 1) {
#     if (bomb[i][0] === 0 && bomb[i][1] === 0) {
#       safeboard[bomb[i][0]][bomb[i][1] + 1] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1]] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1] + 1] = 1;
#     } else if (bomb[i][0] === 0 && bomb[i][1] === board.length - 1) {
#       safeboard[bomb[i][0]][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1]] = 1;
#     } else if (
#       bomb[i][0] === board.length - 1 &&
#       bomb[i][1] === board.length - 1
#     ) {
#       safeboard[bomb[i][0] - 1][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0] - 1][bomb[i][1]] = 1;
#       safeboard[bomb[i][0]][bomb[i][1] - 1] = 1;
#     } else if (bomb[i][0] === board.length - 1 && bomb[i][1] === 0) {
#       safeboard[bomb[i][0] - 1][bomb[i][1]] = 1;
#       safeboard[bomb[i][0] - 1][bomb[i][1] + 1] = 1;
#       safeboard[bomb[i][0]][bomb[i][1] + 1] = 1;
#     } else if (bomb[i][0] === 0) {
#       safeboard[bomb[i][0]][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0]][bomb[i][1] + 1] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1]] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1] + 1] = 1;
#     } else if (bomb[i][0] === board.length - 1) {
#       safeboard[bomb[i][0] - 1][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0] - 1][bomb[i][1]] = 1;
#       safeboard[bomb[i][0] - 1][bomb[i][1] + 1] = 1;
#       safeboard[bomb[i][0]][bomb[i][1] + 1] = 1;
#       safeboard[bomb[i][0]][bomb[i][1] - 1] = 1;
#     } else if (bomb[i][1] === 0) {
#       safeboard[bomb[i][0] - 1][bomb[i][1]] = 1;
#       safeboard[bomb[i][0] - 1][bomb[i][1] + 1] = 1;
#       safeboard[bomb[i][0]][bomb[i][1] + 1] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1]] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1] + 1] = 1;
#     } else if (bomb[i][1] === board.length - 1) {
#       safeboard[bomb[i][0] - 1][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0] - 1][bomb[i][1]] = 1;
#       safeboard[bomb[i][0]][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1]] = 1;
#     } else {
#       safeboard[bomb[i][0] - 1][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0] - 1][bomb[i][1]] = 1;
#       safeboard[bomb[i][0] - 1][bomb[i][1] + 1] = 1;
#       safeboard[bomb[i][0]][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0]][bomb[i][1] + 1] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1] - 1] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1]] = 1;
#       safeboard[bomb[i][0] + 1][bomb[i][1] + 1] = 1;
#     }
#   }
#   return safeboard.flat().filter((el) => el === 0).length;
# }
