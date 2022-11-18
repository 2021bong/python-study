# 문자형

# 문자열 생성
str1 = 'bong'
str2 = "python"
str3 = '''hi'''
str4 = """hello world!"""

# len(str) == str.length (JS)
print(type(str1), type(str2), type(str3), type(str4), sep=' ')
print(len(str1), len(str2), len(str3), len(str4), sep=' ')

# 빈문자열 str() ( int() 형변환과 비슷 )
str_1 = ''
str_2 = str()

print(type(str_1), type(str_2))
print(len(str_1), len(str_2))

# 이스케이프 문자
# \t : tab
# \000 : null 문자

# 파이썬은 indent에 민감하기 때문에 에러가 났다면 줄 시작부분에 띄어쓰기가 없는지 확인해 볼 것!

# Raw string : \를 무시함 -> r'str'
r_str1 = r'D:\user\desktop'
r_str2 = r'\n enter'
print(r_str1, r_str2, sep='\n')
print()
print()
print()

# 멀티라인 입력
# '''나 """를 사용하며 \를 사용하여 값을 다음 줄로 내릴 수 있다.
m_str1 = '''hello
world
!'''
m_str2 = \
"""
today
is
221118"""
print(m_str1, m_str2, sep='\n')

# \를 넣으면 다른 문자를 바인딩하므로 여러개를 붙일 수 있다. 변수는 하나 이상은 안되는 것 같다...
multi_test1 = \
'r_str1' \
'r_str2'
  
multi_test2 = \
r_str1 \
    
print(multi_test1, multi_test2)
print()
print()
print()

# 문자열 연산
# + : 문자열이 합해짐
# * n : 문자열이 n번 반복됨
# char in str : char라는 문자가 str 안에 포함되어 있는지 확인 (시퀀스들은 in 연산자를 사용할 수 있음)
# char not in str : in 연산자의 반대 값
str__1 = 'h'
str__2 = 'e'
str__3 = 'l'
str__4 = 'o'
str__5 = 'hello world!'

print(str__1 + str__2 + str__3 * 2 + str__4)
print('!' in str__5, 'a' in str__5, 'a' not in str__5, sep='\n')

# 문자열 형변환
print(str(100), type(str(100)), sep='=>')
print(str(True), type(str(True)), sep='=>')
print()
print()
print()


# 문자열 함수

# str.capitalize() : 첫 글자를 대문자로 바꿔줌
# str.upper() : 글자를 대문자로 바꿔줌 == String.toUpperCase() (JS)
# str.lower() : 글자를 소문자로 바꿔줌 == String.toLowerCase() (JS)
print('abcd'.capitalize())
print('abcd'.upper())
print('ABCD'.lower())

# str.startswith('char') : str이 char문자로 시작하는지를 판별 == String.startsWith() (JS)
# str.endswith('char') : str이 char문자로 끝나는지를 판별 == String.endsWith() (JS)
print('hello world'.startswith('h'))
print('hello world'.startswith('l'))
print('hello world'.endswith('d'))
print('hello world'.endswith('l'))

# str.replace('find char','change char') : 원하는 문자로 변경 == String.replace() (JS)
print('I\'m good'.replace('o', '0'))

# sorted(str) : 문자열을 받아서 정렬한 뒤 리스트로 반환함
print(sorted('xasbsee'))

# str.split('char') : str을 char를 기준으로 나누어 리스트로 반환 == String.split() (JS)
print('h e ll o'.split(' '))

# dir(str) : 파이썬 내장함수, 객체의 속성 목록을 보여줌 == 모듈에서 정의하는 이름들을 확인하기 위해서 사용 -> str에서 이용할 수 있는 메소드들을 모두 보여줌, import한 뒤 모듈을 확인할 때 사용하는 듯
print(dir('hello'))
print()
print()
print()
# __iter__가 있으면 반복(시퀀스)이 가능하다
# 이터러블이어야 반복이 가능하다..? 역시 기본 개념은 다 비슷한 것 같다~
for i in 'hello world':
  print(i)

print()
print()
print()
  
# 슬라이싱
print('hello world'[0:3]) # 2번째 인덱스의 -1까지 나옴 == str.slice(0, 3) (JS)
print('hello world'[3:]) # 2번째 인덱스를 주지않으면 끝까지 나옴 == str.slice(3) (JS)

h_w = 'hello world'
print(h_w[:len(h_w)]) # 1번째 인덱스를 비워 줄 수도 있다. 모든 길이를 보여줌 == str.slice(0, str.length()) (JS)
print(h_w[1:len(h_w):2]) # 3번째 인자를 주면 해당 간격만큼 가져온다.
print(h_w[-3:]) # 음수도 가능하며 뒤에서 부터 센다.
print(h_w[1:-2])
print(h_w[::3]) # 앞을 비워두고 세번째 인자만 줄 수도 있다.
print(h_w[::-2]) # 세번째에 음수를 주변 오른쪽에서 왼쪽으로 가져온다.
# 앞에 인자를 비워줘도 된다니... 혁명이다..... 파이썬 짱......

# 아스키코드
print(ord('A')) # 문자 -> 아스키 == str.charCodeAt() (JS)
print(chr(90)) # 아스키 -> 문자 == String.fromCharCode(str) (JS)