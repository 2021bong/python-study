# [1차]비밀지도

# 첫번째 풀이
def solution(n, arr1, arr2):
  answer = []
  for i in range(n):
    if len(bin((arr1[i])|arr2[i])[2:]) != n:
      answer.append('0'* (n - len(bin((arr1[i])|arr2[i])[2:]) )+ bin((arr1[i])|arr2[i])[2:])
  #   answer.append(bin((arr1[i])|arr2[i])[2:].rjust(n,'0')) -> rjust를 사용하니 코드가 짧아진다!
      continue
    answer.append(bin((arr1[i])|arr2[i])[2:])
  for i in range(n):
    answer[i] = answer[i].replace('1', '#').replace('0', ' ')
  return answer

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))



#  다른 사람의 풀이 1
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
# zip()
# 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
# 양 측에 있는 데이터를 하나씩 차례로 짝을 지어준다.
# a = [1, 2, 3]
# b = ['A', 'B', 'C']
# for n, s in zip(a, b):
#   print(n,'과', s)

# str.rjust(자릿수, 채울문자) : 문자열을 오른쪽으로 정렬하여 원하는 길이만큼 공백에 문자를 넣어준다.
# 왼쪽으로 정렬하는 ljust도 있다.
# str.zfill(자릿수) : 자릿수를 넣으면 왼쪽으로 0을 채워준다.



# 다른 사람의 풀이 2
def solution(n, arr1, arr2):
    answer = []
    for index in range(0,n):
        answer.append(str(bin(arr1[index] | arr2[index] | pow(2,n))).replace("0b1","").replace("1","#").replace("0"," ")) # 애초에 자릿수를 맞춰주려고 제곱근을 사용해서 한자리 길게 만들고 0b1를 없앴다.
        pass # pass는 왜 사용했을까..?

    return answer
# pow(x, y) : x의 y 제곱

# pass vs continue
# pass : 실행할 코드가 없는 것으로 다음 코드가 실행된다.
# continue : 다음 loop로 넘어간다.
# pass를 사용할 때
# 조건문에 넣어줄 조건이 딱히 없을 경우, class 선언할 때 어떠한 내부 구문도 필요 없을 때 (넣어주지 않으면 에러가 발생하기 때문)
# 나중에 코드를 추가할 계획이거나
# 일단 코드를 작성한 후 동작 확인을 위해서
# 예외가 발생했을 때 처리하되 아무 수행을 하지 않고 무시할 때