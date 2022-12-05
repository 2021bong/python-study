# 겹치는 선분의 길이

# sort() : 리스트 내장 메소드, 정렬해줌, 리스트 자체를 정렬
# y = [lines[0][1],lines[1][1],lines[2][1]]
# y.sort()
# sorted() : 어떤 이터러블 객체던 정렬해줌, 정렬된 새로운 리스트를 반환
# x = sorted([lines[0][0],lines[1][0],lines[2][0]])

# python vs JS
# list.append() vs array.push()


# sum : list의 합을 구해줌
# sum(list)


def solution(lines):
    x = sorted([lines[0][0],lines[1][0],lines[2][0]])
    y = sorted([lines[0][1],lines[1][1],lines[2][1]])
    ans = []
    if x[0] <= x[1]:
      if y[0] - x[1] > 0:
        ans.append(y[0] - x[1])
        
    if x[2] >= x[1]:
      if y[1] - x[2] > 0:
        ans.append(y[1] - x[2])
        
    if y[0] > x[2]:
      if y[0] - x[2] > 0:
        ans.append((y[0] - x[2]) * - 1)
        
    return sum(ans)
    
lines1 = [[0, 1], [2, 5], [3, 9]]
lines2 = [[-1, 1], [1, 3], [3, 9]]
lines3 = [[0, 5], [3, 9], [1, 10]]

print(solution(lines1))
print(solution(lines2))
print(solution(lines3))

# JS 풀이
# function solution(lines) {
#     const x = [lines[0][0],lines[1][0],lines[2][0]].sort((a, b)=>a - b)
#     const y = [lines[0][1],lines[1][1],lines[2][1]].sort((a, b)=>a - b)
#     let ans = [];
#     if (x[0] <= x[1]) {
#         if (y[0] - x[1] > 0){
#         ans.push(y[0] - x[1])
#         }
#     }
#     if (x[2] >= x[1]) {
#         if (y[1] - x[2] > 0){
#         ans.push(y[1] - x[2])
#         }
#     }
#     if (y[0] > x[2]) {
#         if (y[0] - x[2] > 0){
#         ans.push((y[0] - x[2]) * - 1)
#         }
#     }
#     return ans.reduce((acc, cur)=>acc + cur, 0)
# }
