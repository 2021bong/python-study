# 최빈값 구하기

# sorted와 lambda
# sorted([list 혹은 dic], key = lambda x: [key로 지정하고 싶은 요소])

# sorted는 원본을 바꾸지 않고 새로운 요소를 반환하는 것 같아서 재할당을 해줬다.

def solution(array):
  if len(array) == 1:
    return array[0]
  
  setArr = set(array)
  numList = []
  for value in setArr:
    numList.append([value, 0])
    
  for num1 in array:
    for num2 in numList:
      if num1 == num2[0]:
        num2[1] += 1
        break
  
  numList = sorted(numList, key = lambda x : -x[1])
  
  # numList의 길이가 1인 경우 처리를 안해줘서 런타임 에러 발생
  if len(numList) >= 2 and numList[0][1] == numList[1][1]:
    return -1
  else:
    return numList[0][0]

# print(solution([1, 2, 3, 3, 3, 4]))
# print(solution([1, 1, 2, 2]))
# print(solution([1]))