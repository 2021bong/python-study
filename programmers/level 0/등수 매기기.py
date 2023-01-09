# 등수 매기기

# sort() : 기준에 따라 오름차순 또는 내림차순 정렬
# sort(reverse=True) : 내림차순 정렬
# reverse() : 단순히 리스트의 순서를 뒤집는 것

# list.index() == (JS) indexOf()
# 특정 원소가 몇번째에 등장했는지 알려줌, 중복이면 맨 첫 인덱스를 출력

# 첫번째 풀이
# def solution(score):
#   for i in range(len(score)):
#     score[i] = int(sum(score[i]) / 2)
#   sortScore = score.copy()
#   sortScore.sort(reverse=True)
#   for i in range(len(score)):
#     for j in range(len(sortScore)):
#       if score[i] == sortScore[j]:
#         score[i] = j + 1
#         break
#   return score

# 남의 풀이를 참고했으나 2,3,6 런타임 에러
# def solution(score):
#   avg = []
#   ans = []
#   for i in range(len(score)):
#     avg.append(int(sum(score[i]) / 2))
#   avg.sort(reverse=True)
#   for i in score:
#     ans.append((avg.index((i[0] + i[1])/2)) + 1)
#   return ans

def solution(score):
  # 어차피 합이 같으면 평균도 같기에 굳이 평균을 직접적으로 구하지 않은 것 같음
  # 또한 []를 이용해서 짧게 코드를 적을 수 있는 것 같음, Lazy evaluation이라고 하는 것 같다.
  avg = sorted([sum(i) for i in score], reverse = True)
  ans =[]
  for i in score:
    ans.append((avg.index(sum(i))) + 1)
  return ans

print(solution([[80, 60], [50, 50], [30, 70], [70, 30]]))
print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))

# JS풀이 (통과)
# function solution(score) {
#   const avg = score.map((el) => (el[0] + el[1]) / 2);
#   const seq = [...avg].sort((a, b) => b - a);
#   for (let i = 0; i < avg.length; i += 1) {
#     for (let j = 0; j < seq.length; j += 1) {
#       if (avg[i] === seq[j]) {
#         avg[i] = j + 1;
#         break;
#       }
#     }
#   }
#   return avg;
# }
