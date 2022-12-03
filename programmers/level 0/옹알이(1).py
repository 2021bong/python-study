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
# & 연산자가 있던데 나중에 찾아봐야겠음

# 밸류와 인덱스를 같이 이용하기
# for 인덱스, 밸류 in enumerate(이터러블객체):

case1 = ["aya", "yee", "u", "maa", "wyeoo"];
case2 = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"];

def solution(babbling):
  can = ["aya", "ye", "woo", "ma"]
  newbabbling = [];
  
  for i in babbling:
    if len(i) <= 10 and len(i) >= 2:
      newbabbling.append(i)

  for i, value in enumerate(newbabbling):
    for j in can: 
      if value.find(j) != -1 :
        newbabbling[i] = newbabbling[i].replace(j, '')
  answer = [];
  for i in newbabbling:
    if len(i) == 0:
      answer.append(i)
  
  return len(answer);

# 파이썬 테스트 케이스 6, 7 통과 못함

  
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