def make_html_text(name, fortune, list):
    head = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>안녕하세요! {0}님 새해를 맞이하면서 세웠던 계획들 기억하시나요?</title>
  </head>
  <body style="background-color: #E8F1F6;">
    <table
      border="0"
      cellpadding="0"
      cellspacing="0"
      style="text-align: center; color: #000; width: 100%;
      margin: 0 auto;
      max-width: 350px;
      background-color: #E8F1F6;"
    >
      <tr>
        <td style=" width: 100%;
        max-width: 350px;
        height: 100px;
        padding-top: 36px;"><img style=" max-width: 350px;" src="https://res.cloudinary.com/dsm9617cz/image/upload/v1686837817/kkachi-admin/thmywmpnvathukydkdzw.png" alt="올해까치 배너"></td>
      </tr>
'''.format(name)
    greeting = '''<tr>
        <td style="padding: 24px 16px 36px 16px;
        text-align: center;
        font-weight: 400;
        font-size: 14px;
        line-height: 24px;">
          <p style="margin: 0;">안녕하세요! {0}님.
            <br />
            새해에 세웠던 계획들 기억하시나요?<br />약속드린 데로 까치가 {0}님의 목표를 다시 알려드리기 위해 찾아왔어요!
          </p>
        </td>
      </tr>
      <tr>
        <td>
          <img src="https://res.cloudinary.com/dsm9617cz/image/upload/v1686840173/kkachi-admin/tfnqqrkjs3fdiuqlyrwp.png" style="width: 34px;
          height: auto;
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
        fortune_for_kor = "연애/결혼"
        fortune_desc = '내 운명반쪽을 찾아서'
        card_img = 'https://res.cloudinary.com/dsm9617cz/image/upload/v1675320353/kkachi-admin/x8ehy8kur4sunabwwfcw.jpg'
    elif int(fortune) == 2:
        fortune_for_kor = "재물/돈"
        fortune_desc = '올해는 주머니 두둑한 부자'
        card_img = 'https://res.cloudinary.com/dsm9617cz/image/upload/v1675320353/kkachi-admin/jmrasep5ubgegzgicsvg.jpg'
    elif int(fortune) == 3:
        fortune_for_kor = "대인관계"
        fortune_desc = '넓게 두텁게 다양하게 평화롭게'
        card_img = 'https://res.cloudinary.com/dsm9617cz/image/upload/v1675320353/kkachi-admin/vv4oz0ed5vkg8ducsafw.jpg'
    elif int(fortune) == 4:
        fortune_for_kor = "자아실현"
        fortune_desc = '보람차고 성장하는 한 해'
        card_img = 'https://res.cloudinary.com/dsm9617cz/image/upload/v1675320353/kkachi-admin/jjh5uugt0rpckr0n9dsy.jpg'
    else:
        fortune_for_kor = "건강"
        fortune_desc = '건강한 몸 건강한 정신'
        card_img = 'https://res.cloudinary.com/dsm9617cz/image/upload/v1675320353/kkachi-admin/ed6ssirkcy6h7pn5joi7.jpg'
    fortune = ''' <tr>
        <td>
          <img src="{0}" style=" width: 311px;
          height: 447px;
          margin-top: 24px;
          "></img>
        </td>
      </tr>
      <tr>
        <td>
          <p style="margin: 0; margin-top: 24px;
          font-weight: 800;
          font-size: 16px;
          line-height: 24px;">까치에게 바랬던 새해 복 : {1}</p>
          <p style="margin: 0; margin-top: 4px;
          margin-bottom: 36px;
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
            border-bottom: 1px solid #79A8D6; padding-top: 0;">{0}</li>'''.format(
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
            border-bottom: 1px solid #fff; margin-bottom: 36px;
            padding-bottom: 0;
            border: none;">{0}</li>'''.format(text)
        else:
            goal_list += '''<li style="margin: 0;
            list-style: none;
            margin: 0 28px;
            padding: 12px 0;
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
            border-bottom: 1px solid #79A8D6;">{0}</li>'''.format(text)
    goals = '''
      <tr>
        <td>
          <ul style="margin: 0;
          padding: 0;
          list-style: none;">
            <h2 style="margin-top: 36px;
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
        <td style="padding: 36px 16px 56px 16px;
        font-weight: 400;
        font-size: 14px;
        line-height: 24px;">혹시나 바쁜 일상 속에서 잠시 잊고 계셨다면<br />이 메일이 도움이 되셨길 바랍니다. <br />남은 한 해 계획한 것 모두 이루시길 바라며<br />까치가 응원합니다!</td>
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
        <p style="margin: 0; margin-bottom: 12px;">본 메일은 1회에 한하여 전송되는 이메일 입니다.<br />이후 저장된 정보는 모두 폐기됩니다.</p>
          <p style="margin: 0;">올해까치<br /><a href="mailto:10004team@gmail.com" target="_blank" style="text-decoration: none; color: #757575;">10004team@gmail.com</a></p>
        </div>
      </td>
      </tr>
    </table>
  </body>
</html>
    '''

    mytext = head + greeting + fortune + goals + saygoodbye
    return mytext
