def solution(survey, choices):
    scores = [0, 3, 2, 1, 0, 1, 2, 3]
    count = {'A':0, 'N':0, 'C':0, 'F':0, 'M':0, 'J':0, 'R':0, 'T':0}
    for i in range(len(survey)):
      if choices[i] > 4:
        count[survey[i][1]] += scores[choices[i]]
      elif choices[i] == 4:
        continue
      else: 
        count[survey[i][0]] += scores[choices[i]]
    type = ''
    if count['R'] < count['T']:
      type += 'T'
    else:
      type += 'R'
    if count['C'] < count['F']:
      type += 'F'
    else:
      type += 'C'
    if count['J'] < count['M']:
      type += 'M'
    else:
      type += 'J'
    if count['A'] < count['N']:
      type += 'N'
    else:
      type += 'A'
    return type

# print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))
# print(solution(["TR", "RT", "TR"],[7, 1, 3]))



# 다른 사람 풀이
def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys(): # 정해 둔 점수 목록의 키와 일치하지 않으면
            A = A[::-1] # 유형타입을 반대로 뒤집음 -> 'RT' => 'TR'
            my_dict[A] -= B-4 # 뒤집으면 정해둔 타입과는 반대의 점수를 얻게 됨
        else:
            my_dict[A] += B-4 # 정해둔 위치와 똑같으면 위치에 맞게 점수가 들어감 (R타입은 음수로 처리, T타입은 양수로 처리)

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0: # 키의 1번 인덱스 글자의 점수가 더 높을 때
            result += name[1]
        elif my_dict[name] < 0: # 키의 0번 인덱스 글자의 점수가 더 높을 때
            result += name[0]
        else:
            result += sorted(name)[0] # sorted를 문자열에 사용하면 한글자씩 분리하여 정렬된 배열을 반환함 -> 알파벳 순 해결

    return result
