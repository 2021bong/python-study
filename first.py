# 파이썬 주석은 '#'
print('study start\n\nhi')
print("study start")
print('''study start''')
print("""study start""")


# seperator option -> sep에 들어간 문자열과 함께 합해짐, Array.join()과 비슷한 것 같음
print('s','t','a','r','t', sep=',')


# end option
# print는 기본으로는 줄바꿈을 해주지만
# end 옵션이 있으면 줄바꿈이 없고 해당하는 문자로 끝내서 다음 print문과 이어준다.
print('hi', end=' ')
print('python', end='!')
print()


# file option
# 특정한 파일에 내가 적은 내용을 적을것이다.
import sys

print('file import', file=sys.stdout)
# stdout = 콘솔의 아웃

# 예
# print('file import', file='text.txt')


# format 사용 (d : 정수, s : 문자열, f : 실수(소수 float))

# c 언어처럼 데이터타입을 정하고 넣어주는 방법같음
print('%s %s' % ('one','two'))

print('%s %s' % ('index', 3)) # 왜 두개 다 실행될까..?
print('%s %d' % ('index', 3))

# 들어갈 위치를 정해주고 format에 들어오는 인자를 순서대로 넣어줌
print('{} {}'.format('one','two'))

print('{} {} {}'.format('one','two','three'))

# 들어갈 위치에 format에 들어오는 인자의 인덱스를 넣어서 위지를 바꿀수도 있음
print('{1} {0}'.format('one','two'))

print('{2} {0} {1}'.format('one','two','three'))

# %s
# 10길이의 s를 출력 -> 길이가 모자르면 앞에 공백을 채우고 글자를 출력, 오른쪽으로 정렬
# format 도 위와 같음
print('%10s' % ('hi'))
print('{:>10}'.format('hi'))

# 이건 별 의미가 없네...
print('{:<7}'.format('hihihihihi'))

# 이렇게 하면 반대..! 10자리수인데 왼쪽부터 정렬
print('%-10s' % ('hi'))
print('{:10}'.format('hi'))

# 문자를 하나 넣으면 공백대신 그 문자로 채워짐
print('{:->10}'.format('hi'))

# 이렇게하면 에러가 나네용 ㅎㅎ
# print('{:-$>10}'.format('hi'))

# 중앙 정렬
print('{:^10}'.format('hi'))

# 절삭, 슬라이스 -> .
print('%.5s' % 'hihihiho')
print('%5s' % 'hihihiho')
# 10개의 공간중에 5개만 보여줘라! 그래서 공백은 남아있음 총 길이는 10. 위는 총길이도 5
print('{:10.5}'.format('hihihiho'))

# %d
# 문자와 같지만 {}.format을 사용할 때 정수는 d를 붙여줘야함
print('%5d' % 123)
print('{:5d}'.format(123))

# %f
# 소수도 f를 명시적으로 표현해줘야함
# 이렇게 하면 다 안나옴 -> 1.1234567
print('%f' % 1.123456789)
print('{:f}'.format(1.123456789))
# 그래서 보여줄 길이를 정할 수 있음 -> %정수개수.소수개수f
print('%1.9f' % 1.123456789)
# 더 길게도 가능
print('%1.12f' % 1.123456789)

# 자리수 지정
# 총 6자리인데 그 중 소수는 3자리를 차지하고 모자란건 0으로 채워라 -> 자리수에는 .도 포함
# mysql demical과 비슷한 방식 같음
print('%06.3f' % 1.123456789)
print('%05.1f' % 1.123456789)
