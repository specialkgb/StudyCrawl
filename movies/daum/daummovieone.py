import requests
from bs4 import BeautifulSoup
import movies.persistence.MongoDAO as DAO

# 객체생성
mDao = DAO.MongoDAO()

cnt = 0
page = 1
while True:
    list_url = 'https://movie.daum.net/moviedb/grade?movieId=126335&type=netizen&page={}'.format(page)
    resp = requests.get(list_url)

    soup = BeautifulSoup(resp.text, 'html.parser')


    if resp.status_code != 200:
        print('WARNING: 잘못된 URL 접근')

    reply_list = soup.select('div.review_info')

    if len(reply_list) == 0:
        print('더이상 댓글이 없습니다.')
        break
    print(page, 'Last page')

    for reply in reply_list:
        cnt += 1
        writer = reply.select('em.link_profile')[0].text.strip()
        score = reply.select('em.emph_grade')[0].text.strip()
        review = reply.select('p.desc_review')[0].text.strip()
        rgdt = reply.select('span.info_append')[0].text.strip()
        print('=================================================')
        print('작성자:', writer)
        print('평점', score)
        print('리뷰', review)
        index_val = rgdt.index(',')
        print('날짜', rgdt[:index_val])
        print()

        # MongoDB에 저장하기 위해 Dict Type으로 변환!
        data = {'content': review,
                'writer': writer,
                'score': score,
                'reg_date': rgdt}

        # 내용, 작성자, 평점, 작성일자 MongoDB에 Save
        mDao.mongo_write(data)

    page += 1

    print('수집한 댓글은 총 {}건 입니다.'.format(cnt))

