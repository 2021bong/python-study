# 2016년

import datetime
def solution(a, b):
    return datetime.datetime(2016,a,b).strftime('%a').upper()

# 나는 모듈을 import해서 금방 풀었는데 치열하게 푼 사람이 많았다.. 대단하다
# 모듈을 쓰지 않은 짧은 풀이들은 인자로 들어온 날까지 총 몇일인지 합을 구하고
# 7로 나눠서 숫자에 대한 요일을 반환했다. (2016년 1월 1일의 요일은 금요일이고 2016년은 윤년이므로)

# print(solution(5, 24))