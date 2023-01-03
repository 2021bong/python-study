# while

# while <exp>:
#    <statememt(s)>

# break, continue
m = 5
while m > 0:
  m = m - 1
  if m == 3:
    continue
  if m == 0:
    break
  print(m)
  
print()
print()
print()


# while - else
n = 10
while n > 0:
  n -= 1
  print(n)
  if n == 5:
    break
else: # while문이 다 끝마쳐지고 나면 실행됨. 하지만 break로 빠져나오면 실행되지 않음. 
  print('else')
  
names = ['김','이','봉']
i = 0
while i < len(names):
  print(names[i])
  i += 1
else:
  print('출석 끝')
  
print()
print()
print()

arr = ['김','이','봉']
while True:
  if not arr:
    break
  print(arr.pop(-1))
  print(arr)