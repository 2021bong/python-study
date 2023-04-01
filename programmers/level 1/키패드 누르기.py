# 키패드 누르기

def solution(numbers, hand):
    hand = hand[0:1].upper()
    left_num = [1, 4, 7]
    right_num = [3, 6, 9]
    phone = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,2)]
    thmb_L = 10
    thmb_R = 11
    answer = []
    for n in numbers:
      if n in left_num:
        thmb_L = n
        answer.append('L')
      elif n in right_num:
        thmb_R = n
        answer.append('R')
      else:
        sum_L = abs(phone[n][0] - phone[thmb_L][0]) + abs(phone[n][1] - phone[thmb_L][1])
        sum_R = abs(phone[n][0] - phone[thmb_R][0]) + abs(phone[n][1] - phone[thmb_R][1])
        if sum_L < sum_R:
          thmb_L = n
          answer.append('L')
        elif sum_L == sum_R:
          if hand == 'L': thmb_L = n
          else: thmb_R = n
          answer.append(hand)
        else:
          thmb_R = n
          answer.append('R')
          
    return ''.join(answer)
    
# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
