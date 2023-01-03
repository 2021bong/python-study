word = 'hello world'
print(word.capitalize()) # 첫글자만 대문자
print(word.title()) # 단어의 첫글자만 대문자
text = ' hello world '
print(text.strip(' '))
text2 = '0hello world0'
print(text.strip('0'))
print()

# strip : 인자로 전달된 문자를 str의 양쪽(왼쪽, 오른쪽)에서 제거
# lstrip : 인자로 전달된 문자를 str의 왼쪽에서 제거
# rstrip : 인자로 전달된 문자를 str의 오른쪽에서 제거
text0 = '0야호0'
print(text0.strip('0'))
print(text0.lstrip('0'))
print(text0.rstrip('0'))