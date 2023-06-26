from process_data_01 import process_data
from make_html_text_02 import make_html_text
from send_email_03 import send_email


def email_automation(db_data):
    for i in db_data:
        processed_data = process_data(i)
        name, email, fortune, goals = processed_data["name"], processed_data[
            "email"], processed_data["fortune"], processed_data["goals"]
        # name, fortune, list
        html_text = make_html_text(name, fortune, goals)
        # name, html_text, to_email
        send_email(name, html_text, email)


db_data = [
    {
        "id": 1,
        "nickname": "봉까치",
        "email": "test123@test.co.kr",
        "fortune_id": 2,
        "goals": [
            "자유의 몸 되기"
        ]
    }
]

email_automation(db_data)
