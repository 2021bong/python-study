from email_automation import send_email
csv_text = '''홍길동,my_email@naver.com,health,"["의적질하기", "새 구름 장만하기", "운동하기"]"
봉길동,my_email@naver.com,money,"["부자되기", "국내든 해외든 친구들이랑 여행가기", "유튜브 시작하기", "이모지 테스트⭐️"]"
뿡뿡이,my_email@naver.com,money,"["english text"]"
방구쟁이,my_email@naver.com,ego,"["방구쟁이", "뿡뿡이", "뿡뿌르 뿡뿡뿡", "행복하세요?", "긴 문장은 어떻게 되는지 실험해보겠습니다. 이게 몇자?"]"'''

csv_arr = csv_text.split('\n')
for i in range(len(csv_arr)):
    csv_arr[i] = csv_arr[i].replace(' "', '')
    csv_arr[i] = csv_arr[i].replace('"', '')
    csv_arr[i] = csv_arr[i].replace('[', '')
    csv_arr[i] = csv_arr[i].replace(']', '')
    split_arr = csv_arr[i].split(',')
    data = csv_arr[i].split(',')
    goals_arr = []
    for j in range(3, len(data)):
        goals_arr.append(data[j])
    csv_arr[i] = {"nickname": data[0], "email": data[1],
                  "fortune": data[2], "goals": goals_arr}

json_arr = [{
    "nickname": "홍길동",
    "email": "my_email@naver.com",
    "fortune": "health",
    "goals": "[\"의적질하기\", \"새 구름 장만하기\", \"운동하기\"]",
},
    {
    "nickname": "봉길동",
    "email": "my_email@naver.com",
    "fortune": "money",
    "goals": "[\"부자되기\", \"국내든 해외든 친구들이랑 여행가기\", \"유튜브 시작하기\", \"영어회화와 일본어회화 공부하기\", \"이모지 테스트⭐️\"]",

},
    {
    "nickname": "뿡뿡이",
    "email": "my_email@naver.com",
    "fortune": "money",
    "goals": "[\"english text\"]",
},
    {
    "nickname": "방구쟁이",
    "email": "my_email@naver.com",
    "fortune": "ego",
    "goals": "[\"방구쟁이\", \"뿡뿡이\", \"긴 문장은 어떻게 되는지 실험해보겠습니다. 이게 몇자?\"]",
}]

for i in range(len(json_arr)):
    json_arr[i]['goals'] = str(json_arr[i]['goals'][2:-2]).split('", "')

# for data in csv_arr:
#     send_email(data)

for data in json_arr:
    send_email(data)
