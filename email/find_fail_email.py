message = '''
success_email@gmail.com | 정상적으로 메일이 발송되었습니다.
fail@gmail.com | 받으실 메일 주소를 정확히 입력하십시오.
'''

msgArr = message.split('\n')
print(len(msgArr))
for i, text in enumerate(msgArr):
    if "받으실 메일 주소를 정확히 입력하십시오" in text:
        print(i, text)
