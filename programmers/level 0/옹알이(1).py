# 옹알이 (1)
# str.find('찾을 문자열') # 찾는 문자열의 첫글자 인덱스를 반환, 없으면 -1을 반환 (JS indexOf와 비슷)
# str.index('찾을 문자열') # 찾는 문자열의 첫글자 인덱스를 반환, 없으면 오류를 발생 (try ~ except 구문으로 감싸서 처리를 해줘야 함)

# 파이썬 falsy (이외에는 모두 truthy)
# False
# None
# 0, 0.0, 0L, 0j
# ""
# []
# ()
# {}

# replace
# 변수.replace(old, new, [count])
# 변수.replace(변경하고 싶은 문자, 변경할 문자, 횟수)

# join
# 구분자.join(list)

# 비교연산자 (PYTHON vs JS)
# and vs &&
# or vs ||

# 밸류와 인덱스를 같이 이용하기
# for 인덱스, 밸류 in enumerate(이터러블객체):

case1 = ["aya", "yee", "u", "maa", "wyeoo"];
case2 = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"];
case3 = ["ayaaya", "wooaya", 'yayae', 'woyeo', 'yewmaya' ];

# 첫번째 풀이 (케이스 6, 7 통과 못함)
# def solution(babbling):
#   can = ["aya", "ye", "woo", "ma"]
#   newbabbling = [];
  
#   for i in babbling:
#     if len(i) <= 10 and len(i) >= 2:
#       newbabbling.append(i)

#   for i, value in enumerate(newbabbling):
#     for j in can: 
#       if value.find(j) != -1 :
#         newbabbling[i] = newbabbling[i].replace(j, '')
#   answer = [];
#   for i in newbabbling:
#     if len(i) == 0:
#       answer.append(i)
  
#   return len(answer);


# 다른 사람 풀이 참고
def solution(babbling):
  can = ["aya", "ye", "woo", "ma"]
  ans = 0
  for i in babbling:
    for j in can: 
      i = i.replace(j, '?')
    if i.replace('?','') == '':
      ans += 1
  return ans

# 빈문자열('')로 치환해버렸을 때 'yayae'같은 단어가 불가능한 발음으로 세어져야하는데 발음되는 단어로 세져서 그런 것 같음
# JS에서는 '?'로 바꾼 뒤에 ''로 바꿨기 때문에 통과가 된 것 같음
# 머리를 굴려서 예외케이스 단어를 만들어 넣어도 잘 되는데 대체 6,7번 케이스 단어가 뭘까....?
def solution(babbling):
  can = ["aya", "ye", "woo", "ma"]
  newbabbling = [];
  
  for i in babbling:
    if len(i) <= 10 and len(i) >= 2:
      newbabbling.append(i)

  for i, value in enumerate(newbabbling):
    for j in can: 
      if value.find(j) != -1 :
        newbabbling[i] = newbabbling[i].replace(j, '?')
  answer = 0;
  for i in newbabbling:
    if i.replace('?','') == '':
      answer += 1
  
  return answer;

# print(solution(case1))
# print(solution(case2))
# print(solution(case3))



# ------------------------------------------------------
# & :  비트 연산자
# 두개의 이진수에서 동일한 위치의 bit가 1인 것들만 1로 계산 -> 이걸 어디에 쓰는걸까.....????

# result = 7 & 2
# print(result)
#         7 = 0000 0111
#      &  2 = 0000 0010
#-----------------------
# result, 2 = 0000 0010 
# ------------------------------------------------------
  
# JS 풀이
# function solution(babbling) {
#   const can = ["aya", "ye", "woo", "ma"]
#   babbling = babbling.filter((word)=>(can.join('').length >= word.length) && (word.length >= 2))

#   for(let i = 0 ; i < babbling.length; i+=1){
#       for (let j = 0; j < can.length; j+=1){
#           if(babbling[i].includes(can[j])) {
#           babbling[i] = babbling[i].replace(can[j],'?')
#           }
#       }
#   }
#   const answer = babbling.map((el)=> [...el].map((el)=>el === '?' ? '' : el).join('')).filter((el)=>el.length === 0)

#   return answer.length;
# }