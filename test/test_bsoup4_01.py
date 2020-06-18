import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/read.nhn?mode=LS2D&mid=shm&sid1=103&sid2=248&oid=056&aid=0010852631'
# url사이트에 get방식으로 requests를 하면
# return으로 사이트의 html code를 전달

resp = requests.get(url)

if resp.status_code == 200: #reques 코드가 200번대에는 정상이고 400, 600은 비정상이니까 표시를 하라는 코드임.
    resp.headers
else:
    print('잘못된 URL입니다. 다시 입력해주세요.')

soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.find('h3', id='articleTitle')
contents = soup.find('div', id='articleBodyContents')
print(title.text) # .text를 붙이면 주소를 제외한 텍스트 제목만 출력하고 title만 쓰면 소스 주소까지 출력한다.
print()
print(contents.text)