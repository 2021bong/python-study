def send_email(email_data):
    import smtplib
    import re
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    # from email.mime.image import MIMEImage  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈

    def sendEmail(addr):
        reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
        if re.match(reg, addr):
            smtp.sendmail(my_account, to_mail, msg.as_string())
            print("정상적으로 메일이 발송되었습니다.")  # 전송 되면 console에 뜸
        else:
            print("받으실 메일 주소를 정확히 입력하십시오.")

    # smpt 서버와 연결
    gmail_smtp = "smtp.gmail.com"
    gmail_port = 465
    smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)

    # 로그인
    my_account = "my_email@gmail.com"
    my_password = "app password"
    smtp.login(my_account, my_password)

    # 메일을 받을 계정
    to_mail = email_data["email"]

    # 메일 기본 정보 설정
    msg = MIMEMultipart()
    msg["Subject"] = "안녕하세요. 까악까악"  # 메일 제목
    msg["From"] = my_account
    msg["To"] = to_mail

    # 메일 본문 내용
    str_goals = '\n'.join(email_data["goals"])
    content = "안녕하세요. \n\n %s님! \n %s \n\n 기억나세요?" % (
        email_data["nickname"], str_goals)
    content_part = MIMEText(content, "plain")
    msg.attach(content_part)

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
