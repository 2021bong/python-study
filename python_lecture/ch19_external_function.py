# 파이썬 외장 함수
# sys, pickle, shutil, temfile, time, random 등


# sys
import sys
print(sys.argv) # 명령행 인자 받기
# sys.exit() # 강제 종료
print(sys.path) # 파이썬 패키지 위치


# pickle : 객체 파일 쓰기
import pickle
f = open("file.obj", "wb")
content = {1: "hi", 2: "hello"}
pickle.dump(content, f)  # dump : 쓸 때
f.close()  # open 했으면 close 해야 함

# 파일 읽기
f = open("file.obj", "rb")
data = pickle.load(f)  # load : 읽을 때
print(data)
f.close()


# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
import os
print(os.environ)
print(os.environ["USER"])
print(os.getcwd())  # 현재 경로


# time : 시간 관련 처리
import time
print(time.time()) # 현재 시간
print(time.localtime(time.time())) # 형태 변환
print(time.ctime()) # 간단 표현
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 원하는 형식
# time.sleep() # 시간 간격 발생 (setTimeout이랑 비슷한건가..?)
# for i in range(5):
#   print(i)
#   time.sleep(3)


# random : 난수 리턴
import random
print(random.random()) # 0 ~ 1 실수
print(random.randint(1, 100)) # 1부터 100까지 정수
print(random.randrange(1, 100)) # 1부터 99까지 정수
test = [1,2,3,4,5]
random.shuffle(test) # 순서를 섞어 줌
print(test)
pick = random.choice(test) # 랜덤 선택
print(pick)


# webbrowser
import webbrowser
# webbrowser.open("https://google.com") # 기본 브라우저에서 열기
# webbrowser.open_new("https://google.com") # 새창에서 열기