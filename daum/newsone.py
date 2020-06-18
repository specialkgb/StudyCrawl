# 다음에서 뉴스 한 건의 기사와 내용을 수집
import requests
from bs4 import BeautifulSoup
# url은 내가 수집하고 싶은 데이터가 위치한 웹사이트 주소를 가리킴!
url = 'https://news.v.daum.net/v/20200616090601222'
# url주소를 이용해서 해당 웹페이지의 모든 소스코드를 불러와서 resp에 저장
resp = requests.get(url)

if resp.status_code == 200:
    print('Success')
else:
    print('Wong URL')
# requests는 소스코드만 전부 가져오는 거고 거기서 원하는 내용을 추출 불가!!
# 원하는 내용만 추출하려면 beautifulsoup을 사용해야함.
# beautifulsoup에 input으로 resp의 값(웹사이트의 소스코드 전체)을 전달
# soup에 웹사이트의 소스코드 전체가 저장
# soup.select()를 이용하여 원하는 정보만 추출
soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.select('h3.tit_view') #(태그+선택자)
                                   # #id값이면 "#" 을 쓴다. 클래스 값이면 "." 을 쓴다.


print(title[0].text)

contents = soup.select('div#harmonyContainer p') # 자손을 긁을려면 한칸 띄고 p
# soup.select()는 무조건 return을 list type으로 반환
# [val1, val2, val3, ...]
# ex) contents[1]

print()

text = ''
for i in contents:
    text += i.text

print(text) # strip()은 공백제거 코드이나 사이사이에 있는 공백은 제거할 수 없다.