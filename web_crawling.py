import requests
import json


def get_data(url):
    resp = requests.get(url)
    html = resp.text
    with open('./data.json', 'w', encoding='utf8') as j1:
        j1.write(html)

    with open('./data.json', encoding='utf8') as json_file:
        json_data = json.load(json_file)

        for item in json_data["items"]:
            print(item["reviewTitle"])

            with open('./data.txt', 'a', encoding='utf8') as f2:
                f2.write("리뷰제목 :" + " " + item["reviewTitle"] + " " + "리뷰내용 :" + " " +
                         item["reviewText"] + " " + "도움받은 사람 수 :" + " " + str(item["helpfulYes"]) + '\n')


#review
first_url = "https://kr.iherb.com/ugc/api/review?pid=64006&limit=10&lc=ko-KR&translations=ko-KR&page=1&sortId=6&withUgcSummary=true"
test_url = 'https://kr.iherb.com/ugc/api/review?pid=64006&limit=10&lc=ko-KR&translations=ko-KR'
resp = requests.get(first_url)
html = resp.text
total_count = 0
with open('./first.json', 'w', encoding='utf8') as j1:
    j1.write(html)
with open('./data.json', encoding='utf8') as json_file:
    json_data = json.load(json_file)
    total_count = json_data["totalCount"]


with open('./data.txt', 'w') as f1:
    f1.write('')

for i in range(1, int(total_count / 10) + 1):
    url = test_url + '&page=' + str(i) + "&sortId=6&withUgcSummary=true"
    print('url: "' + url + '" 파싱 중...')
    get_data(url)