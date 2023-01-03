import math

f = 1.2345
# round(num, 소수점 자리수)) : 소수점 자리수를 정해 반올림
print(round(10, 2))

i = 16
# math.sqrt(num) : num의 제곱근을 구흠 --import math 필요
print(math.sqrt(i))

# num**num 제곱
print(i ** 2)

# math.pi : 15자리까지 파이값을 반환 --import math 필요
print(math.pi)

print()

# ch27
# num = float(input("3자리 이상의 소수를 입력해주세요. : "))
# print(num * 2)

# ch28
# num = float(input("3자리 이상의 소수를 입력해주세요. : "))
# print(round(num * 2, 2))

# ch29
# num = int(input("500 이상의 정수를 입력해주세요. :"))
# print(round(math.sqrt(num),2))

# ch30
# print(round(math.pi, 5))

# ch31
# radius = int(input("원의 반지름을 입력해주세요. :"))
# print(math.pi * (radius ** 2))

# ch32
# radius = float(input("원기둥의 반지름을 입력해주세요. :"))
# height = float(input("원기둥의 깊이를 입력해주세요. :"))
# print(round((math.pi * (radius ** 2)) * height, 3))

# ch33
# num1 = int(input("숫자를 입력해주세요. :"))
# num2 = int(input("숫자를 하나 더 입력해주세요. :"))
# n = num1 // num2
# rest = num1 % num2
# print(num1,'을 ',num2,'로 나누면 몫은 ',n,'이고 나머지는 ',rest,'입니다.')

# ch34
# print('1. 사각형')
# print('2. 삼각형')
# print()
# num = int(input("번호를 입력해주세요. :"))
# if num == 1:
#   rec = int(input("한 변의 길이를 입력해주세요. :"))
#   print(rec * rec)
# elif num == 2:
#   tri1 = int(input("밑변의 길이를 입력해주세요. :"))
#   tri2 = int(input("높이의 길이를 입력해주세요. :"))
#   print((tri1 * tri2) / 2)
# else:
#   print("잘못된 값을 입력하셨습니다.")