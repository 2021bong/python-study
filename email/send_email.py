def send_email(input_text):
    import smtplib
    import re
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    # from email.mime.image import MIMEImage  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈

    def sendEmail(addr):
        reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
        if re.match(reg, addr):
            smtp.sendmail(my_account, to_mail, msg.as_string())
            print(to_mail, ' | ', "정상적으로 메일이 발송되었습니다.")  # 전송 되면 console에 뜸
        else:
            print(to_mail, ' | ', "받으실 메일 주소를 정확히 입력하십시오.")

    # smpt 서버와 연결
    gmail_smtp = "smtp.gmail.com"
    gmail_port = 465
    smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)

    # 로그인
    my_account = "my_email@gmail.com"
    my_password = "app_pw"
    smtp.login(my_account, my_password)

    # 메일을 받을 계정
    to_mail = "to_email@naver.com"

    # 메일 기본 정보 설정
    msg = MIMEMultipart()
    msg["Subject"] = "안녕하세요. 제가 왔어요~ 😊"  # 메일 제목
    msg["From"] = my_account
    msg["To"] = to_mail

    # 메일 본문 내용
    htmltext = MIMEText(
        input_text, 'html')  # html을 넣어서 보낼때는 타입을 지정해서 MIMEText을 사용해야하는 듯
    msg.attach(htmltext)

    # # 이미지 파일 추가
    # image_name = "test.png"
    # with open(image_name, 'rb') as file:
    #     img = MIMEImage(file.read())
    #     img.add_header('Content-Disposition', 'attachment', filename=image_name)
    #     msg.attach(img)

    # 받는 메일 유효성 검사 거친 후 메일 전송
    sendEmail(to_mail)

    # smtp 서버 연결 해제
    smtp.quit()
