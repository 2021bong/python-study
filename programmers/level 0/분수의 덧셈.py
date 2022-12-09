# 분수의 덧셈

# 파이썬 while문
# while 반복할조건:
#   동작1
#   동작2

# 최소 공약수 -> 유클리드 호제법

# 재귀함수를 이용하는 법
# def gcdRecursive(x, y):
#   if y == 0:
#     return x
#   else :
#     return gcd(x, x % y)

# while문을 이용하는 법
# def gcdWhile(x, y):
#   r
#   while y > 0:
#     r = x % y
#     x = y
#     y = r
#   return x


def solution(denum1, num1, denum2, num2):
    num = num1 * num2
    denum = denum1 * num2 + denum2 * num1
    gcd = 0
    x = 0
    y = 0
    if denum > num:
      x = denum
      y = num
    else :
      x = num
      y = denum
    while y > 0 :
      gcd = x % y
      x = y
      y = gcd
    return [int(denum / x), int(num / x)]
    
print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))

# JS 풀이

# function solution(denum1, num1, denum2, num2) {
#     let num = num1 * num2
#     let denum = denum1 * num2 + denum2 * num1;
#     let gcd = 0;
#     let x = 0;
#     let y = 0;
#     if (denum > num) {
#         x = denum;
#         y = num
#     } else {
#         x = num;
#         y = denum;
#     }    
#     while (y > 0) {
#         gcd = x % y;
#         x = y;
#         y = gcd;
#     }
#     denum = denum / x;
#     num = num / x
#     return [denum, num];
# }