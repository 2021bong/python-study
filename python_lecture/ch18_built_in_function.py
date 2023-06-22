# built in function 내장 함수
# 자주 사용하는 내장 함수

# 절대값
# abs()
print(abs(-3))


# all : 요소가 모두 참인지
# any : 요소가 하나라도 참인지
# iterable 요소 검사
print(all([1, 2, 3]))
print(all([1, 2, 0]))
print(any([1, 2, 3]))
print(any([1, 2, 0]))


# chr() : 아스키 -> 문자
# ord() : 문자 -> 아스키


# enumerate (*중요)
# 인덱스 + Iterable 객체 생성
for i, str in enumerate(['a', 'b', 'c']):
    print(i, 'and', str)


# filter (*중요)
# 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
# filter(함수, 객체 요소) <- 호출하지않고 함수만 넣어줌
def bigger_ten(num):
    return num > 10


print(filter(bigger_ten, [5, 20, 30]))  # 이렇게만하면 filter 객체가 들어오기 때문에 형변환을 해줘야함
print(list(filter(bigger_ten, [5, 20, 30])))
print(list(filter(lambda x: x > 10, [5, 20, 30])))  # lambda도 사용 가능


# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id('5'))


# len : 요소의 길이 반환
print(len('123455667'))
print(len([1, 2, 3]))


# max : 최대값
# min : 최소값
print(max([1, 2, 3]), min([1, 2, 3]))
print(max('abcde'), min('abcde'))


# map (*중요)
# 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conver_abs(n):
    return abs(n)


print(list(map(conver_abs, [-1, -2, -3, 1, 2, 3])))
print(list(map(lambda x: abs(x), [-1, -2, -3, 1, 2, 3])))

# pow 제곱값 반환
# pow(제곱할 값, 몇 제곱)
print(pow(2, 10))


# range : 반복 가능한 객체 반환
print(list(range(1, 10)))
print(list(range(1, 10, 2)))
print(list(range(1, -10, -2)))


# round : 반올림
# round(반올림할 수, 소수점 자리수)
print(round(1.555, 3))
print(round(1.555))  # 정하지 않으면 소수점 첫째 자리에서 반올림


# sorted : 반복가능한 객체 정렬 후 반환
# 조건을 다양하게 줄 수 있음
# sort도 있음
print(sorted([3, 6, 12, 8, 2, 1, 4]))


# sum : 반복가능한 객체의 합 반환
print(sum([1, 2, 3]))


# type : 자료형 확인


# zip : 반복가능한 객체의 요소를 묶어서 반환
# 길이가 다르면 짝이 맞는 부분까지 묶음
print(dict(zip([1, 2, 3], ['a', 'b', 'c'])))  # zip 객체가 반환되어 형변환 해줘야함
