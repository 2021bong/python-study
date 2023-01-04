# 16진수
n = 5
print('%x'%n) # 16진수 소문자
print('%X'%n) # 16진수 대문자

# 8진수
print('%o'%n)
print()

# 유니코드 
s1 = 'A'
print(ord(s1)) # == str.charCodeAt() (JS)
s2 = 65
print(chr(s2)) # == str.fromCharCode() (JS)

# 부호를 바꿔서 출력하기
n = 5
print(-n)

# 문자 여러번 출력하기
n = 1
s = 'Hello'
print(s * n)