# 행맨 만들기
import time
import csv
import random
# import winsound # 윈도우 사운드 모듈

# 이름 입력받고 인사 및 로딩 띄우기
# name = input("Hello, What's your name? :D \n")

# print()
# print("Nice to meet you,", name)
# print("Let's start! :)")
# print()

# print("...START LOADING...")

# time.sleep(1)

words = []

# with open('./python_lecture/file/quiz_list.txt') as file: # output 실행
with open('./file/quiz_list.txt') as file:  # 파일 직접 실행
    reader = csv.reader(file)
    for ans in reader:
        words.append(ans)

random.shuffle(words)
choicedAnswer = random.choice(words)

# 정답
answer = choicedAnswer[0].strip().upper()

user_answer = ""

life = 10

while life > 0:
    print()
    correct = 0
    for c in answer:
        if c.upper() in user_answer:
            print(c.upper(), end=' ')
            correct += 1
        else:
            print("_", end=' ')

    if correct == len(answer):
        print()
        # winsound.PlaySound('경로', winsound.SND_FILENAME) 맥에서는 사용 불가능 ㅠㅠ
        print("Congratulations, You are winner! ;D")
        break

    print()
    print("* HINT :", choicedAnswer[1].strip().upper())
    user_input = input("guess the answer : ").upper()
    user_answer += user_input

    if user_input not in answer:
        life -= 1
        print()
        print("Oops!", user_input, "is Wrong.")
        print()
        print("You have", life, "life.")

        if life == 0:
            print()
            print("You are lose, Bye :(")
