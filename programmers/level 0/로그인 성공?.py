# 로그인 성공?

def solution(id_pw, db):
    id, pw = id_pw
    for data in db:
      if data[0] == id:
        if data[1] == pw:
          return 'login'
        else:
          return 'wrong pw'
    return 'fail'
    
# print(solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
# print(solution(["programmer01", "15789"],[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
# print(solution(["rabbit04", "98761"],[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))