# [1차] 다트 게임

def solution(dartResult):
    list_dart = [i for i in dartResult]
    times = {'S':1, 'D': 2, 'T':3}
    bonus = {'*':2, '#':-1}
    total = []
    score = 0
    for i in range(len(list_dart)):
      if list_dart[i] in bonus:
        if list_dart[i] == '*' and len(total) > 0:
          total[len(total)-1] *= 2
          score *= bonus[list_dart[i]]
          total.append(score)
          score = 0
          continue
        score *= bonus[list_dart[i]]
        total.append(score)
        score = 0
      else:
        if list_dart[i] in times:
          score **= int(times[list_dart[i]])
          if i + 1 < len(list_dart) and list_dart[i + 1] in bonus:
            continue
          total.append(score)
        else:
          if i != 0 and (list_dart[i-1]) == '1' and list_dart[i] == '0':
            score = 10
            continue  
          score = int(list_dart[i])
    return sum(total)
  
# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
# print(solution('1D2S3T*'))



# 다른 사람 풀이 1
import re # 정규표현식 모듈a
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)') # re.compile(패턴) : 정규표현식을 패턴 문자열을 컴파일하여 정규표현 패턴 오브젝트를 생성, 동일 패턴을 반복사용시 편리함
    dart = p.findall(dartResult) # findall(대상) : 정규표현식과 매치된 부분 모두 리스트로 반환, [(),(),()]형태로 반환됨
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0: # 튜플이므로 인덱스로 접근 가능
            dart[i-1] *= 2 # 이전 값은 이미 숫자로 바꿔뒀기때문에 *2를 하면 됨
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]] # 튜플 자리수에 맞춰 값을 계산해 숫자로 변경

    answer = sum(dart)
    return answer
  
  
  
# 다른 사람 풀이 2
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k') # 10을 1,0이 아니라 아예 한덩이(10)로 바꾸고 시작한다.
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1) # 3. 인덱스 + 1을 점수로 취급
        elif j == '*':
            answer[i] = answer[i] * 2 # 4 - 1. 지금 값 2배
            if i != 0 : # 4 - 1 - 1. answer의 길이가 0이 아니면 이전 값까지 2배
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)  # 4 - 2. 지금 값 -1배
        else:
            answer.append(int(j)) # 1. 일단 숫자를 answer에 추가
            i += 1 # 2. answer에 접근 가능한 인덱스 == 지금 넣는 값
    return sum(answer)