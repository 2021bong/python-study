import random

# random.random() : 0과 1사이의 임의의 부동소수점 생성
print(random.random())

# random.randint(num1, num2) : num1와 num2 사이의 임의의 정수를 선택
print(random.randint(1, 100))

# random.randrange(num1, num2, 증가값) : num1부터 num2사이에서 증가값만큼 증가하는 수 중에 임의의 숫자를 선택한다.(2의 배수, 5의 배수 ...)
print(random.randrange(0, 100, 5))

# 큰 부동소수 구하기
num1 = random.randrange(1, 100)
num2 = random.randrange(1, 100)
newf = num1 / num2
print(newf)

# random.choice([list]) : list의 요소 중 임의의 요소를 선택
print(random.choice(['red','green','yellow','blue']))
print()

# ch52
# print(random.randint(1, 101))

# ch53
# print(random.choice(['apple','banana','pear','pineapple','tangerine']))

# ch54
# com = random.choice(['h','t'])
# user = input("h와 t중에 하나를 골라주세요. :")
# if user != 'h' and user != 't':
#   print('잘못 입력하셨습니다. 다시 입력해주세요.')
# else:
#   if com == user:
#     print('당신이 이겼습니다.')
#     print('computer :', com)
#   else:
#     print('당신이 졌습니다.')
#     print('computer :', com)

# ch55
# rannum = random.randint(1, 6)
# usernum = int(input("1부터 6사이의 숫자를 하나 선택해주세요. :"))
# if rannum == usernum:
#   print('당신이 이겼습니다!')
# else:
#   if rannum > usernum:
#     print('더 큰 수입니다.')
#   else:
#     print('더 작은 수입니다.')
#   usernum = int(input("1부터 6사이의 숫자를 다시 선택해주세요. :"))

# if rannum == usernum:
#   print('당신이 이겼습니다!')
# else:
#   print('당신이 졌습니다.', rannum)

# ch56
# rannum = random.randint(1, 11)
# correct = False
# while not correct:
#   usernum = int(input("1과 10사이의 숫자를 입력하세요. :"))
#   if rannum == usernum:
#     print("정답입니다.")
#     correct = True

# ch57
# rannum = random.randrange(1, 11)
# correct = False
# while not correct:
#   usernum = int(input("1과 10사이의 숫자를 다시 입력하세요. :"))
#   if rannum == usernum:
#     print("정답입니다.")
#     correct = True
#   elif rannum > usernum:
#     print('더 큰 수입니다.')
#   else:
#     print('더 작은 수입니다.')

# ch58
# score = 0
# for q in range(1, 6):
#   num1 = random.randrange(0, 100)
#   num2 = random.randrange(0, 100)
#   ans = num1 + num2
#   user = int(input(str(num1)+'+'+str(num2)+'= ? :'))
#   if ans == user:
#     score += 1

# print(score,'개 맞췄습니다.')

# ch59
# com = random.choice(['red','green','yellow','blue'])
# correct = False
# while not correct:
#   user = input("'red','green','yellow','blue', 이 중 한가지 색을 다시 골라보세요. :")
#   if com == user:
#     print('정답입니다.')
#     correct = True
#   else:
#     if user =='red':
#       print('지금 화가 나셨나요?')
#     elif user == 'green':
#       print('혹시 이름이 김가인인가요?')
#     elif user == 'yellow':
#       print('당신은 바나나를 좋아해요. 맞죠?')
#     elif user == 'blue':
#       print('지금 슬프신가요?')

