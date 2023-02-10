# package(패키지)
# 모듈을 모아놓은 폴더
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성

import sys
sys.path.append('/Users/bong-wonhui/Documents/MyProject/python-study')

# import만 쓸때는 경로포함 풀네임을 써줘야함
# <syntax> import 가져올 모듈

# from : 폴더 경로가 길 경우 사용
# <syntax> from 폴더경로(패키지) import 가져올 모듈 as 별칭

# import \*
# \*로 import하는 것은 불필요하게 많은 것을 가져오므로 되도록 사용하지 않는 것이 좋다.
# \*로 가져오면 하위에 있는 모든 파일 이름으로 접근 가능하다

import ch15_module
from ch_test.ch16_test import ch16_test
from playground import 별찍기 as star
ch16_test()

# __init__.py
# 파이썬 3.3부터는 없어도 패키지로 인식 -> 하위 호환을 위해 작성 추천
# 구버전에서는 __all__ 변수의 list안에 패키지에 있는 모든 모듈의 이름을 적어줘야 import할 수 있다.
# 외부에서 모듈을 사용할 수 있도록 허가내주는 역할이라고 생각하면 된다.

