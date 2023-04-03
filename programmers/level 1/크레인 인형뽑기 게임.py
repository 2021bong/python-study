# 크레인 인형뽑기 게임

def solution(board, moves):
    board = [b for b in board if b.count(0) != len(board)] # -> 이 코드를 빼니까 시간이 더 줄어들음. 굳이 넣을 필요없을 듯.
    basket = []
    count = 0
    for m in moves:
      for l in range(len(board)):
        if board[l][m-1] != 0:
          basket.insert(0, board[l][m-1])
          board[l][m-1] = 0
          if len(basket) >= 2 and basket[0] == basket[1]:
            count += 2
            basket = basket[2:]
          break
    
    return count
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.05ms, 10.2MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (2.88ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.14ms, 10.3MB)
# 테스트 8 〉	통과 (0.73ms, 10.2MB)
# 테스트 9 〉	통과 (0.30ms, 10.2MB)
# 테스트 10 〉	통과 (0.56ms, 10.3MB)
# 테스트 11 〉	통과 (0.79ms, 10.4MB)

# 첫 줄 코드 뺀거 -> 2중 for문을 쓰려고 하면 무턱대고 시간이 오래걸린다고 생각해버리니까 비효율적으로 풀게 되는 것 같다.
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (1.53ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.04ms, 10.1MB)
# 테스트 7 〉	통과 (0.16ms, 10.3MB)
# 테스트 8 〉	통과 (0.67ms, 10.3MB)
# 테스트 9 〉	통과 (0.57ms, 10.2MB)
# 테스트 10 〉	통과 (0.35ms, 10.1MB)
# 테스트 11 〉	통과 (0.75ms, 10MB)
  
# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

# 다른 사람 풀이 -> 나랑 똑같은 풀인데 insert대신 append를 썼다.
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (1.23ms, 10.1MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.08ms, 10.1MB)
# 테스트 8 〉	통과 (0.30ms, 10.2MB)
# 테스트 9 〉	통과 (0.28ms, 10.2MB)
# 테스트 10 〉	통과 (0.35ms, 10.1MB)
# 테스트 11 〉	통과 (0.71ms, 10.2MB)