# 다음에서 뉴스 한 페이지의  기사와 내용을 수집
import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

url_list = soup.select('ul.list_allnews a.link_txt') # 여러 링크를 가져오고 싶을 경우 그 링크들만 속한 그룹 태그를 찾는다.

for i in url_list:
    url = i['href'] # 앵커 태그만 쭉 뽑아오는 방법
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = soup.select('h3.tit_view')
    contents = soup.select('div#harmonyContainer p')

    text = ''
    for i in contents:
        text += i.text
    print('')
    print()
    print(title[0].text)
    print()
    print(text)
    print()
