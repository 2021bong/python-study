from process_data_01 import process_data
from make_html_text_02 import make_html_text
from send_email_03 import send_email


def email_automation():
    return "email"


list_arr = ['한달에 40만원씩 저축해서 연말에 이탈리아 해외여행 가기',
            '매일 아침 10분씩 스트레칭 하기', '에프터이팩트 강의 결제해서 일주일에 2개씩 듣고 완강하기']
html_text = make_html_text('홍길동', 4, list_arr)
send_email('홍길동', html_text, "to_email@gmail.com")
