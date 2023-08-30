# 파일 읽기 및 쓰기

# 읽기 모드 : r
# 쓰기 모드 : w
# 추가 모드 : a
# 텍스트 모드 : t
# 바이너리 모드 : b


# 예제 1 - 파일 읽기
# 텍스트는 기본 값이므로 rt를 r로 생략해서 사용할 수 있다.
import os
f = open('./python_lecture/file/sample.txt', 'r', encoding='UTF-8')
# 속성확인
# print(dir(f))
print('인코딩 :', f.encoding)
print('경로포함이름 :', f.name)
print('파일이름 :', os.path.basename(f.name))
print('모드 :', f.mode)
text = f.read()
print('파일 내용 :', text)
# 꼭 리소스 닫기
f.close()
print()


# 예제2 - 파일 읽기
# with문과 as를 사용해서 편하게 파일을 읽을 수 있다. with문을 나오면 알아서 리소스를 정리해준다.
with open('./python_lecture/file/sample.txt', 'r', encoding='UTF-8') as file:
    print(file.encoding)
    print(file.name)
    print(os.path.basename(file.name))
    print(file.mode)
    print(file.read())


# 예제3 - 파일 일부만 읽기
# read()에 인자로 숫자를 넘기면 해당 개수만큼 읽어온다.
# 커서가 마지막으로 읽은 곳을 기억하고 있기 때문에 여러번 사용하면 이어서 읽는다.
# seek()을 사용하면 커서 위치를 재설정한다.
with open('./python_lecture/file/sample.txt', 'r', encoding='UTF-8') as file:
    print(file.read(4))
    print(file.read(4))
    file.seek(0, 0)
    print(file.read(4))
print()


# 예제4 - 한 줄씩 읽기
with open('./python_lecture/file/sample.txt', 'r', encoding='UTF-8') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
print('--------')


# 예제5 - 전체를 읽은 후 라인 단위로 리스트로 저장
with open('./python_lecture/file/sample.txt', 'r', encoding='UTF-8') as file:
    for t in file.readlines():
        print(t, end='야호')
    print(file.readlines())  # 이미 파일을 다 읽었기 때문에 커서가 끝에 있어서 빈 리스트가 출력된다.
print()

# 예제6 - 파일 쓰기
# 쓰기 모드일 때도 t는 생략 가능하다.
# w면 파일이 새로 덮어 씌워진다.
with open('./python_lecture/file/sample.txt', 'w') as file:
    file.write('샘플 텍스트입니다.\n')
    file.write('가나다라마바사\n')
    file.write('abcdefg\n')
    file.write('1234567\n')
# a면 파일에 추가 된다.
with open('./python_lecture/file/sample.txt', 'a') as file:
    file.write('방명록 남깁니다~\n')


# 예제7 - 리스트를 파일에 쓰기
with open('./python_lecture/file/sample.txt', 'a') as file:
    list1 = ['하이\n', '안녕\n', '곤니치와\n', '니하오\n']
    list2 = ['하이', '안녕', '곤니치와', '니하오']
    file.writelines(list1)
    file.writelines(list2)


# 예제8 - print로 파일 쓰기
with open('./python_lecture/file/sample.txt', 'a') as file:
    print('\n', file=file)
    print('HELLO', file=file)
    print('OLLEH', file=file)
    print('HHH', file=file)
