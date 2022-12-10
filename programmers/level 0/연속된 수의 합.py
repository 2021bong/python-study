# 연속된 수의 합

# 역순 반복문
# range의 step을 -1로 하기
# for i in (n, 0, -1):
#   print(i)
# reversed()이용하기 -> 리스트의 원소를 거꾸로 뒤집고 이를 반환함
# for i in reversed(range(n)):
#   print(i)

# 오름차순 정렬
# list.sort()

# map
# 반환값이 map객체이므로 원하는 자료형으로 변환시켜줘야함
# list(map(function, iterable))

def solution(num, total):
    answer = []
    for i in reversed(range(num)):
      answer.append(i - 1)
    
    answer.sort()
    ansTotal = sum(answer)
    avg = int((total - ansTotal) / num);
    def add(n):
      return n + avg
    return list(map(add, answer))
  
# print(solution(3, 12))
# print(solution(5, 15))

# JS 풀이
# function solution(num, total) {
#     let diff = [];
#     for (let i = num ; i > 0; i-=1){
#         diff.push(i - 1)
#     }
#     diff.sort((a, b)=> a - b)
#     const diffTotal = diff.reduce((acc, cur)=>acc + cur)
#     const one = (total - diffTotal) / num;
#     diff = diff.map((num)=>num + one)
#     return diff
# }