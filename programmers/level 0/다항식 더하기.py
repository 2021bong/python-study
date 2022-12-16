# 다항식 더하기

def solution(polynomial):
    if len(polynomial) == 1 or len(polynomial) == 2:
        return polynomial
    xNum = []
    num =  []
    for v in polynomial.split(' + '):
      if 'x' in v:
        if v == 'x':
          xNum.append(1)
        else:
          xNum.append(int(v.split('x')[0]))
      else:
        num.append(int(v))
  
    if len(xNum) != 0 and len(num) != 0:
      xNum = sum(xNum)
      num = sum(num)
    elif len(xNum) == 0:
      return sum(num)
    elif len(num) == 0:
      return str(sum(xNum))+'x'
      
    ans = [str(xNum), 'x', ' + ', str(num)]
    return ''.join(ans)
    

print(solution("3x + 7 + x"))
print(solution("x + x + x"))

# JS풀이 (5, 8, 12 통과 못함)

# function solution(polynomial) {
#     if (polynomial.length === 1 || polynomial.length === 2) return polynomial;
#     const splitStr = polynomial.split(' + ')
#     let xNum = [];
#     let num = [];
#     for (let i = 0 ; i < splitStr.length; i+=1){
#         splitStr[i].includes('x') ? xNum.push(splitStr[i].length === 1 ? 1 : splitStr[i].split('x')[0]) : num.push(splitStr[i])
#     }
#     xNum = xNum.length != 0 && xNum.reduce((acc, cur)=> Number(acc) + Number(cur)) + 'x';
#     num = num.length != 0 && num.reduce((acc, cur)=> Number(acc) + Number(cur));
    
#     let ans = `${xNum} + ${num}`
#     if (!!!xNum) {
#         ans = num
#     }
#     if (!!!num) {
#         ans = xNum
#     }
    
#     return ans
# }