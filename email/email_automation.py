from process_data_01 import process_data
from make_html_text_02 import make_html_text
from send_email_03 import send_email


def email_automation(db_data):
    for i in db_data:
        process_data = process_data(i)
        name, email, fortune, goals = process_data.name, process_data.email, process_data.fortune, process_data.goals
        # name, fortune, list
        html_text = make_html_text(name, fortune, goals)
        # name, html_text, to_email
        send_email(name, html_text, email)


# name : str, fortune: int, list: list, to_email: str
name = "홍길동"
fortune_id = 2
list_arr = ['한달에 40만원씩 저축해서 연말에 이탈리아 해외여행 가기',
            '매일 아침 10분씩 스트레칭 하기', '에프터이팩트 강의 결제해서 일주일에 2개씩 듣고 완강하기']
to_email = "test@email.com"
html_text = make_html_text(name, fortune_id, list_arr)
send_email(name, html_text, to_email)
