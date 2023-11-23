import math
def solution(fees, records): 
  # fee : 기본 시간, 기본 요금, 단위 시간, 단위 요금
    default_time, default_fees, over_time, over_fees = fees
  # records : 시각, 차량번호, 내역
    records = [record.split() for record in records]
    parkinglot = {}
    time_data = {}
    for record in records:
      time, car, type = record
      if type == 'IN':
        if car not in parkinglot:
          h, m = time.split(':')
          start = (int(h) * 60) + int(m)
          parkinglot[car] = start
      else:
        if car in parkinglot:
          h, m = time.split(':')
          end = (int(h) * 60) + int(m)
          start = parkinglot[car]
          use_time = end - start
          if car not in time_data:
            time_data[car] = use_time
          else:
            time_data[car] += use_time
          del parkinglot[car]

    last_time = 23 * 60 + 59
    if parkinglot:
      list_parkinglot = list(parkinglot.items())
      for parking_car in list_parkinglot:
        car, parking_time = parking_car
        use_time = last_time - parking_time
        if car not in time_data:
            time_data[car] = use_time
        else:
            time_data[car] += use_time
    sorted_cars = sorted(list(time_data.items()), key = lambda x : x[0])
    answer = []
    for car in sorted_cars:
      num, time = car
      if time > default_time:
        answer.append(default_fees + math.ceil((time - default_time) / over_time) * over_fees)
      else:
        answer.append(default_fees)
    return answer
# 테스트 1 〉	통과 (0.04ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.07ms, 10.3MB)
# 테스트 4 〉	통과 (0.12ms, 10.4MB)
# 테스트 5 〉	통과 (0.16ms, 10.3MB)
# 테스트 6 〉	통과 (0.17ms, 10.4MB)
# 테스트 7 〉	통과 (2.59ms, 10.6MB)
# 테스트 8 〉	통과 (1.06ms, 10.5MB)
# 테스트 9 〉	통과 (0.16ms, 10.3MB)
# 테스트 10 〉	통과 (1.33ms, 10.6MB)
# 테스트 11 〉	통과 (1.76ms, 10.9MB)
# 테스트 12 〉	통과 (1.86ms, 10.8MB)
# 테스트 13 〉	통과 (0.04ms, 10.4MB)
# 테스트 14 〉	통과 (0.03ms, 10.5MB)
# 테스트 15 〉	통과 (0.04ms, 10.3MB)
# 테스트 16 〉	통과 (0.02ms, 10.3MB)

# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])) # [14600, 34400, 5000]
# print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])) # [0, 591]
# print(solution([1, 461, 1, 10], ["00:00 1234 IN"])) # [14841]


# 다른 사람 풀이
# 클래스를 이용한 풀이
from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees):
        self.fees = fees
        self.in_flag = False # 주차되어있는지
        self.in_time = 0 # 이용 시작 시간
        self.total = 0 # 총 이용 시간

    def update(self, t, inout):
        self.in_flag = True if inout=='IN' else False # in_flag 입차하면 True, 출차하면 False
        if self.in_flag:  self.in_time = str2int(t) # 입차하면 in_time에 시작시간
        else:             self.total  += (str2int(t)-self.in_time) # 출차하면 총 이용 시간은 += 출차 시간 - 입차 시간

    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out') # 입차되어있으면 23:59로 총 이용 시간 계산
        add_t = self.total - self.fees[0] # 추가 요금 내야하는 시간
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1] # 초과시간이 있으면 초과시간 요금 return 없으면 기본 요금 return

def str2int(string):
    return int(string[:2])*60 + int(string[3:]) # str 시간을 바로 숫자(분)로 변환

def solution(fees, records):
    # defaultdict : 값이 있는지 없는지 체크 없이 알아서 key로 생성해줌
    recordsDict = defaultdict(lambda:Parking(fees)) # lambda를 사용해 초기값 지정
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout) # defaultdict를 사용했기때문에 추가하며 update도 사용 가능
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]
# 테스트 1 〉	통과 (0.05ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.06ms, 10.3MB)
# 테스트 4 〉	통과 (0.10ms, 10.3MB)
# 테스트 5 〉	통과 (0.29ms, 10.4MB)
# 테스트 6 〉	통과 (0.31ms, 10.4MB)
# 테스트 7 〉	통과 (2.31ms, 10.4MB)
# 테스트 8 〉	통과 (0.99ms, 10.2MB)
# 테스트 9 〉	통과 (0.32ms, 10.4MB)
# 테스트 10 〉	통과 (1.80ms, 10.5MB)
# 테스트 11 〉	통과 (2.96ms, 10.7MB)
# 테스트 12 〉	통과 (2.95ms, 10.7MB)
# 테스트 13 〉	통과 (0.05ms, 10.5MB)
# 테스트 14 〉	통과 (0.03ms, 10.2MB)
# 테스트 15 〉	통과 (0.03ms, 10.3MB)
# 테스트 16 〉	통과 (0.03ms, 10.3MB)

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])) # [14600, 34400, 5000]
