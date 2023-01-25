# input 
# 사용자 입력 받기

# 변수 = input(사용자에게 보여줄 문자)
# 콘솔은 입력이 불가능한 환경이므로 input()은 콘솔이 아닌 터미널에서 실행해주어야함
name = input('What your name ? : ')
print('Hello,',name,'!')

# 입력 받는 기본 타입 : str
age = input('How old are you ? : ')
print(type(int(age)))
print(type(age))

# format으로 변수 넣기 ==`${변수1}와 ${변수2}`
# 여러번 본 것 같은데 아직도 어색함...
print('FirstName : {0}, LastName : {1}'.format(input('Enter your fisrt name : '), input('Enter your last name : ')))