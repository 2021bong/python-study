# ch1
# userName = input("이름이 무엇인가요? : ")
# print('Hello, ', userName)

# ch2
# firstName = input("이름이 무엇인가요? :")
# lastName = input("성이 무엇인가요? : ")
# print("Hello, ",firstName, lastName)

# ch3
# print("What do you call a bear with no teeth?", '\n', "A gummy bear!")

# ch4
# num1 = int(input("아무 숫자를 주세요! :"))
# num2 = int(input("아무 숫자를 한 번 더 주세요! : "))
# # 형변환을 해주지 않으면 문자가 됨!
# print ("The total is ",num1 + num2)

# ch5
# num1 = int(input("아무 숫자나 주세요! :"))
# num2 = int(input("아무 숫자나 한 번 더 주세요! : "))
# num3 = int(input("곱할 숫자도 주세요! : "))
# print("The answer is ", (num1 + num2)*num3)

# ch6
# wholePizza = int(input("처음에 있던 피자 갯수는 ? : "))
# atePizza = int(input("먹은 피자 갯수는 ? : "))
# print("남은 피자 갯수는", wholePizza - atePizza, '개 입니다.')

# ch7
# name = input("이름이 뭐에요? : ")
# age = int(input("나이가 몇 살 이에요? :"))
# print(name,'next birthday you will be', age + 1)

# ch8
# wholePrice = int(input("총 얼마가 나왔습니까? :"))
# people = int(input("총 몇 명이 왔습니까? :"))
# print('한 사람당',int(wholePrice / people), '원을 내세요.')

# ch9
# getTime = int(input("일 수를 입력하세요. : "))
# hours = getTime * 24
# minute = hours * 60
# second = minute * 60
# print(getTime, "일은 ", hours,'시간, ', minute,"분, ", second,"초 입니다.")

# ch10
# 소수점 자리 제한하기 -> format(제한할 숫자, 제한할 자릿수('.1f','.2f','.3f'))
# pound = 2.204
# weight = int(input("당신의 몸무게는 몇 kg입니까? :"))
# print("당신의 몸무게는 ", format(pound * weight, ".2f"), "파운드입니다.")

# ch11
# 나눗셈 : /
# 몫 : //
# 나머지 : %
# big = int(input("100이 넘는 숫자를 입력해주세요. :"))
# small = int(input("10이 넘지 않는 숫자를 입력해주세요. :"))
# print(big // small)