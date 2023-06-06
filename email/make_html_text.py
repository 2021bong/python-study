from send_email import send_email


def make_html_text(name, fortune, list):
    head = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>안녕하세요. 제가 왔어요~ 😊</title>
  </head>
  <body style="background-color: #e8f1f6">
    <table
      border="0"
      cellpadding="0"
      cellspacing="0"
      style="text-align: center; color: #000; width: 100%;
      margin: 0 auto;
      max-width: 350px;
      font-family: 'NanumSquareNeo';
      background-color: #e8f1f6;"
    >
      <tr>
        <td style=" width: 100%;
        max-width: 350px;
        height: 100px;
        padding-top: 24px;"><img style=" max-width: 350px;" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbupyH4%2FbtsinXRGgSN%2FMwTkSYtinIPPooykqfPKsK%2Fimg.png" alt="올해까치 배너"></td>
      </tr>
'''
    greeting = '''<tr>
        <td style="padding: 24px 16px;
        text-align: center;
        font-weight: 400;
        font-size: 16px;
        line-height: 24px;">
          <p style="margin: 0;">안녕하세요! {0}님.
            <br />
            벌써 올해의 반이 지나가고 있습니다.
          </p>
        </td>
      </tr>
      <tr>
        <td>
          <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcvMnUO%2Fbtsij87F89o%2FfTp2tLf3r1eOOnoy8JtuPk%2Fimg.png" style="width: 34px;
          height: 60px;
          margin-top: 12px;
          margin-bottom: 12px;"
          ></img>
        </td>
      </tr>'''.format(name)
    fortune_for_kor = ''
    fortune_desc = ''
    card_img = ''
    # 1 : love, 2 : money, 3 : relationship, 4 : ego, 5 : health
    if int(fortune) == 1:
        fortune_for_kor = "사랑"
        fortune_desc = '사랑사랑사랑'
        card_img = 'https://res.cloudinary.com/dsm9617cz/image/upload/v1675320353/kkachi-admin/jmrasep5ubgegzgicsvg.jpg'
    elif int(fortune) == 2:
        fortune_for_kor = "재물/돈"
        fortune_desc = '올해는 주머니 두둑한 부자'
        card_img = 'https://res.cloudinary.com/dsm9617cz/image/upload/v1675320353/kkachi-admin/jmrasep5ubgegzgicsvg.jpg'
    elif int(fortune) == 3:
        fortune_for_kor = "인간관계"
        fortune_desc = '친구친구친구'
        card_img = 'https://res.cloudinary.com/dsm9617cz/image/upload/v1675320353/kkachi-admin/jmrasep5ubgegzgicsvg.jpg'
    elif int(fortune) == 4:
        fortune_for_kor = "자아실현"
        fortune_desc = '갓생가보자고~'
        card_img = 'https://res.cloudinary.com/dsm9617cz/image/upload/v1675320353/kkachi-admin/jmrasep5ubgegzgicsvg.jpg'
    else:
        fortune_for_kor = "건강"
        fortune_desc = '건강한 정신 건강한 신체'
        card_img = 'https://res.cloudinary.com/dsm9617cz/image/upload/v1675320353/kkachi-admin/jmrasep5ubgegzgicsvg.jpg'
    fortune = ''' <tr>
        <td>
          <img src="{0}" style=" width: 311px;
          height: 447px;
          margin-top: 24px;"></img>
        </td>
      </tr>
      <tr>
        <td>
          <p style="margin: 0; margin-top: 24px;
          font-weight: 800;
          font-size: 16px;
          line-height: 24px;">까치에게 바랬던 새해 복 : {1}</p>
          <p style="margin: 0; margin-top: 4px;
          margin-bottom: 24px;
  font-weight: 400;
  font-size: 12px;
  line-height: 18px;">{2}</p>
        </td>
      </tr>
      <tr><td><div style="width: 4px;
        height: 4px;
        margin: 0 auto;;
        background: #1B395F;
      border-radius: 4px;"></div></td></tr>'''.format(card_img, fortune_for_kor, fortune_desc)
    goal_list = ''
    for i, text in enumerate(list):
        if (i == 0):
            goal_list += '''<li style="margin: 0;
            padding: 0;
            list-style: none;
            margin: 0 28px;
            padding: 12px 0;
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
            border-bottom: 1px solid #fff; padding-top: 0;">{0}</li>'''.format(
                text)
        elif (i == len(list) - 1):
            goal_list += '''<li style="margin: 0;
            padding: 0;
            list-style: none;
            margin: 0 28px;
            padding: 12px 0;
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
            border-bottom: 1px solid #fff; margin-bottom: 32px;
            padding-bottom: 0;
            border: none;">{0}</li>'''.format(text)
        else:
            goal_list += '''<li style="margin: 0;
            list-style: none;
            margin: 12px 28px 0 12px;
            padding-bottom: 12px;
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
            border-bottom: 1px solid #fff; padding-top: 0;">{0}</li>'''.format(text)
    goals = '''
      <tr>
        <td>
          <ul style="margin: 0;
          padding: 0;
          list-style: none;">
            <h2 style="margin-top: 32px;
            margin-bottom: 24px;
            padding: 0 15px;
          font-weight: 800;
          font-size: 16px;
          line-height: 24px;">{0}님의 올해 목표</h2>
            {1}
          </ul>
        </td>
      </tr>'''.format(name, goal_list)
    saygoodbye = '''
          <tr><td><div style="width: 4px;
        height: 4px;
        margin: 0 auto;;
        background: #1B395F;
      border-radius: 4px;"></div></td></tr>
      <tr>
        <td style="padding: 24px 16px 56px 16px;
        font-weight: 400;
        font-size: 16px;
        line-height: 24px;">감사합니다~</td>
      </tr>
      <tr>
        <td style="padding-bottom: 24px;">
        <div style="margin: 0 16px;
        padding: 24px 0;
        text-align: center;
        border-top: 1px solid #79A8D6;
        color: #757575;
font-weight: 400;
font-size: 12px;
line-height: 18px;">
        <p style="margin: 0; margin-bottom: 12px;">이 메일은 1월에 작성하였던 내용을 토대로 1회에 한하여 자동으로 전송되는 이메일 입니다. 이후 저장된 정보는 모두 폐기됩니다 등의 공지사항 내용입니다.</p>
          <p style="margin: 0;">올해까치<br /><a href="mailto:thisyear@gmail.com" target="_blank" style="text-decoration: none; color: #757575;">thisyear@gmail.com</a></p>
        </div>
      </td>
      </tr>
    </table>
  </body>
</html>
    '''

    mytext = head + greeting + fortune + goals + saygoodbye
    return mytext


fortune_id = 2
list_arr = ['목록 1', '목록 2', '목록3']
html_text = make_html_text('홍길동', 2, list_arr)
send_email(html_text)
