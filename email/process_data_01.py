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

# TODO
# name : str, fortune: int, list: list, to_email: str
# name = "홍길동"
# fortune_id = 2
# list_arr = ['한달에 40만원씩 저축해서 연말에 이탈리아 해외여행 가기',
#             '매일 아침 10분씩 스트레칭 하기', '에프터이팩트 강의 결제해서 일주일에 2개씩 듣고 완강하기']
# to_email = "to_email@gmail.com"


def process_data():
    return "text"
