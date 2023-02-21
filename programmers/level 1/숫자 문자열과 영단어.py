# 숫자 문자열과 영단어

# 첫번째 풀이
def solution(s):
  number_to_str = {
    'zero': 0,
    'one' : 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven' : 7,
    'eight': 8,
    'nine' : 9
  }
  for key in list(number_to_str.keys()):
    if key in s:
      s = s.replace(key, str(number_to_str[key]))   
  return int(s)

# 다른 사람 풀이 참고
def solution(s):
  number_to_str = {
    'zero': '0',
    'one' : '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven' : '7',
    'eight': '8',
    'nine' : '9'
  }
  for key, value in list(number_to_str.items()):
    if key in s:
      s = s.replace(key, value)   
  return int(s)



# 다른 사람의 풀이
# 나처럼 key만 사용한게 아니라 items()로 값까지 사용해 풀었다.
# 처음 숫자도 아예 문자열로 선언했다.
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

# print(solution("one4seveneight"))
# print(solution("23four5six7"))
# print(solution("2three45sixseven"))
# print(solution('123'))