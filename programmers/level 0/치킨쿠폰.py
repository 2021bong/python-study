# 치킨 쿠폰

# 첫 풀이
# def solution(chicken):
#     coupon = chicken
#     bonusChicken = int(coupon // 10)
#     coupon -= bonusChicken * 10
#     coupon += bonusChicken
#     if coupon >= 10:
#       run = True
#       while run:
#         couponChicken = int(coupon // 10)
#         bonusChicken += couponChicken
#         coupon -= couponChicken * 10
#         coupon += couponChicken
#         if coupon < 10:
#           run = False
#     return bonusChicken
  
def solution(chicken):
    coupon = chicken
    bonusChicken = 0
    while coupon > 9:
      couponChicken = int(coupon // 10)
      bonusChicken += couponChicken
      coupon -= couponChicken * 10
      coupon += couponChicken
    return bonusChicken
  
# 아직도 처음부터 while안으로 들어가서 계속 실행되게 하는걸 잘 못하는 것 같다.. 
# while 조건도 잘 못세움 ㅠㅠ 잘 안써서 그런가.. 화이팅
  
print(solution(80))
print(solution(100))
print(solution(1081))
