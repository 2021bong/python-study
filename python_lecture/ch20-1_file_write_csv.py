# csv 읽기 및 쓰기

# CSV : MEME - text/csv

import csv

# 예제1
with open('./python_lecture/file/csv_sample.txt', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Header skip => 커서가 있으므로
    print(reader)
    print(type(reader))
    # print(dir(reader)) # __iter__ => 반복문 사용가능
    print()
    for i in reader:
        print(' : '.join(i))

print()

# 예제2
with open('./python_lecture/file/csv_sample.txt', 'r') as file:
    reader = csv.reader(file, delimiter='|')  # 2번째 인자로 구분자를 지정해서 읽어올 수 있음
    for i in reader:
        print(i[0])

print()

# 예제3
with open('./python_lecture/file/csv_sample.txt', 'r') as file:
    reader = csv.DictReader(file)
    for i in reader:
        # print(i["name"])
        # print(i["age"])
        # print('-----------')
        for n in i.items():
            print(n[0], '||', n[1])
            print('-----------')
        for n, a in i.items():
            print(n, a)
            print('************')

print()
print()
print()

# 예제4
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
with open('./python_lecture/file/csv_sample.txt', 'a', encoding='UTF-8') as file:
    # print(dir(csv))
    writer = csv.writer(file)
    for i in list:
        writer.writerow(i)

# 예제5
key = ['안녕', 'NiHao', 'hello']
with open('./python_lecture/file/csv_write.txt', 'w', encoding='UTF-8') as file:
    dWriter = csv.DictWriter(file, fieldnames=key)  # 1. fieldnames에 지정한 값과
    dWriter.writeheader()

    for v in list:
        dWriter.writerow({key[0]: v[0], key[1]: v[1], key[2]: v[2]})

    # 2. writerow의 값을 매핑함
    for v in list:
        dWriter.writerow({'안녕': v[0]})
    for v in list:
        dWriter.writerow({'hello': v[0], 'NiHao': v[1], '안녕': v[2]})
