# 등수 매기기

# sort() : 기준에 따라 오름차순 또는 내림차순 정렬
# sort(reverse=True) : 내림차순 정렬
# reverse() : 단순히 리스트의 순서를 뒤집는 것

def solution(score):
  for i in range(len(score)):
    score[i] = int(sum(score[i]) / 2)
  sortScore = score.copy()
  sortScore.sort(reverse=True)
  for i in range(len(score)):
    for j in range(len(score)):
      if score[i] == sortScore[j]:
        score[i] = j + 1
        break
  return score
  
print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))