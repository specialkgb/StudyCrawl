import requests
from bs4 import BeautifulSoup

cnt = 0
page = 1
compare_writer = ''
break_point = False # 이중 반복문을 빠져나가기 위한 조건!
while True:
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=191436&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('존재하지 않는 URL')

    soup = BeautifulSoup(resp.text, 'html.parser')
    reply_list = soup.select('div.score_result li')

    for i, reply in enumerate(reply_list):
        content = reply.select('div.score_reple > p > span')[0].text.strip() # 댓글내용
        previous_writer = reply.select('div.score_reple a > span')[0].text.strip()
        cut_index = previous_writer.find('(')  # 작성자에 닉네임만 추출하기위한 index번호 계산
        score = reply.select('div.star_score > em')[0].text.strip() # 평점
        reg_date = reply.select('div.score_reple em')[1].text.strip()[:10] # 작성일자
        # 작성자   # ('span#_filtered_ment' + str(i))  str() > string type 변환 문자열
        # 인덱스 없으면 에러 파인드 인덱스가 없으면 -1
        # 네이버 영화댓글의 작성자는 닉네임(아이디) > 초롱이(cj****) < 구조
        # 위에 예시의 닉네임만 추출 (그러나 닉네임이 없는 경우도 있음)
        # 닉네임이 없는 경우()안의 아이디를 사용하는 코드 작성
        if cut_index > 0:
           writer = previous_writer[:cut_index]
        else:
           writer = previous_writer
        # 지금 작성자 수집 마지막 작성자에 적용시켜야함
        # 네이버 영화댓글 수집 페이지의 마지막 페이지를 계산하는 코드
        # 매 페이지의 첫번째 게시글의 작성자를 compare_writer에 저장하고
        # 매 페이지의 첫번째 게시글 작성자의 compare_writer를 비교해서 같으면 중복페이지
        print('==================================================')
        print('내용', content)
        print('작성자', writer)
        print('평점', score)
        print('작성일자', reg_date)

        if i == 0:
            if compare_writer == writer:
                print('Finished collect :)')
                break_point = True
                break
            else:
                compare_writer = writer
        cnt += 1
    if break_point:
        break
    # 다음페이지 + 1
    page += 1
print('총',cnt,'건을 수집했습니다')
