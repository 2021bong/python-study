# 최소직사각형

# 첫 풀이
def solution(sizes): # 어떤 케이스에서는 이게 더 빠르지만
  for i in sizes:
    i.sort()
  maxW = sorted(sizes, key = lambda x: -x[0])[0][0]
  maxH = sorted(sizes, key = lambda x: -x[1])[0][1]
  return maxW * maxH

# 참고 후 두번째 풀이
def solution(sizes): # 어떤 케이스에서는 이게 더 빠르다. 하지만 몇개의 케이스를 제외하고는 이게 더 빠르다.
  max_list = []
  min_list = []
  for i in sizes:
    max_list.append(max(i))
    min_list.append(min(i))
  return max(max_list) * max(min_list)

# print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
# print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
# print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

# 다른 사람의 풀이
# sizes의 요소인 [w,h]리스트를 돌아
# [둘 중 큰 값]과 [둘 중 작은 값]리스트를 만들고 각각 리스트에서 최대값을 찾아서 곱했다.
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

# 많은 사람들이 max와 min 함수를 많이 사용했다.
# min(iterable, [options]) : 인수로 받은 자료형 내에서 최소값을 찾는다.
# max(iterable, [options]) : 인수로 받은 자료형 내에서 최대값을 찾는다.
# 인자를 여러개를 넣으면 넣은 인자중에 해당하는 값을 찾는다.
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(min(a, b)) # [1,2,3]
# print(max(a, b)) # [4,5,6]

# 한 줄 for문 : [결과 for문]
# list_a = []
# for i in range(10):
#     list_a.append(i) 을

# list_a = [i for i in range(10)] 이렇게 쓸 수 있다.
