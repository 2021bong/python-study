# import sys
# sys.path에 경로를 추가하면 일시적으로 추가되어 import가 가능해짐
# 영구적으로 추가할 땐 별도 설정 필요
import ch15_module # 같은 경로이므로 상관없음
# 파이썬은 JS처럼 별도의 모듈처리 없이 경로만 있으면 파일을 import 할 수 있다.

a = ch15_module.add(2,3)
b = ch15_module.power(2,3)
print(a)
print(b)