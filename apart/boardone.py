# 제목
# 내용
# 작성일자
# 작성자

import requests
from bs4 import BeautifulSoup

url = 'http://news.sarangbang.com/talk/bbs/free/163894?url=%2F%2Fnews.sarangbang.com%2Fbbs.html%3Ftab%3Dfree'
resp = requests.get(url)

if resp.status_code != 200:
    print('WARNING: 잘못된 URL 접근')

soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.select('h3.tit_view')[0].text.strip()
print('TITLE ▶▶▶▶▶', title)

writer = soup.select('a.name_more')[0].text.strip()
print('WRITER ▶▶▶▶▶', writer)

date = soup.select('span.tit_cat')[1].text.strip()[:10]
print('DATE ▶▶▶▶▶', date)

contents = soup.select('div.bbs_view p')

content = ''
for i in contents:
    content += i.text.strip()

print(content)
