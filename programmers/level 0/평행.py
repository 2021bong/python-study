# 평행

def solution(dots):
    first = (dots[0][0]-dots[1][0])/(dots[0][1]-dots[1][1])
    second = (dots[2][0]-dots[3][0])/(dots[2][1]-dots[3][1])
    
    def compare(first, second):
      if first == second :
        return 1
      
    if compare(first, second) == 1:
      return 1

    first = (dots[0][0]-dots[2][0])/(dots[0][1]-dots[2][1])
    second = (dots[1][0]-dots[3][0])/(dots[1][1]-dots[3][1])

    if compare(first, second) == 1:
      return 1
    
    first = (dots[0][0]-dots[3][0])/(dots[0][1]-dots[3][1])
    second = (dots[1][0]-dots[2][0])/(dots[1][1]-dots[2][1])
    
    if compare(first, second) == 1:
      return 1
    
    return 0
    

list1 = [[1, 4], [9, 2], [3, 8], [11, 6]];
list2 = [[3, 5], [4, 1], [2, 4], [5, 10]];
print(solution(list1))
print(solution(list2))

# JS 풀이
# function solution(dots) {
#     let first = (dots[0][0]-dots[1][0])/(dots[0][1]-dots[1][1])
#     let second = (dots[2][0]-dots[3][0])/(dots[2][1]-dots[3][1])

#     const compare = (first, second)=> {
#         if(first === second) {
#             return 1
#         }
#     }

#     if (compare(first, second) === 1) return 1;

#      first = (dots[0][0]-dots[2][0])/(dots[0][1]-dots[2][1])
#      second = (dots[1][0]-dots[3][0])/(dots[1][1]-dots[3][1])

#     if (compare(first, second) === 1) return 1;

#     first = (dots[0][0]-dots[3][0])/(dots[0][1]-dots[3][1])
#      second = (dots[1][0]-dots[2][0])/(dots[1][1]-dots[2][1])

#     if (compare(first, second) === 1) return 1;

#     return 0;
# }