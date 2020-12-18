import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
dbKeyword = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = dbKeyword.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# MongoDB에 insert 하기

db.keywords.insert_one({'keyword' : 'B2B영업'})
db.keywords.insert_one({'keyword' : '전문가영업'})
db.keywords.insert_one({'keyword' : '기술영업'})
db.keywords.insert_one({'keyword' : '글로벌영업'})
db.keywords.insert_one({'keyword' : '세일즈'})
db.keywords.insert_one({'keyword' : 'B2B세일즈'})
db.keywords.insert_one({'keyword' : 'IT영업'})
db.keywords.insert_one({'keyword' : 'SI영업'})
db.keywords.insert_one({'keyword' : '인사이트셀링'})
db.keywords.insert_one({'keyword' : '영업전략'})
db.keywords.insert_one({'keyword' : '선제안영업'})
db.keywords.insert_one({'keyword' : '기업교육'})
db.keywords.insert_one({'keyword' : '영업교육'})
db.keywords.insert_one({'keyword' : '효과적인수주영업'})
db.keywords.insert_one({'keyword' : '제안서교육'})
db.keywords.insert_one({'keyword' : 'B2B세일즈교육'})
db.keywords.insert_one({'keyword' : '세일즈교육'})
db.keywords.insert_one({'keyword' : 'PT교육'})
db.keywords.insert_one({'keyword' : '제안PT'})
db.keywords.insert_one({'keyword' : 'PT코칭'})
db.keywords.insert_one({'keyword' : '협상교육'})
db.keywords.insert_one({'keyword' : '우선협상교육'})
db.keywords.insert_one({'keyword' : '프레젠테이션교육'})
db.keywords.insert_one({'keyword' : 'PT교육'})
db.keywords.insert_one({'keyword' : '우선협상'})
db.keywords.insert_one({'keyword' : '제안서작성교육'})
db.keywords.insert_one({'keyword' : '제안서'})
db.keywords.insert_one({'keyword' : '제안전략'})
db.keywords.insert_one({'keyword' : '선제안'})
db.keywords.insert_one({'keyword' : '수주제안'})
db.keywords.insert_one({'keyword' : '제안서작성'})
db.keywords.insert_one({'keyword' : '제안서강의'})
db.keywords.insert_one({'keyword' : '제안서디자인'})
db.keywords.insert_one({'keyword' : '해외제안서'})
db.keywords.insert_one({'keyword' : '제안서작성법'})
db.keywords.insert_one({'keyword' : '투자제안서'})
db.keywords.insert_one({'keyword' : 'IR자료'})
db.keywords.insert_one({'keyword' : '제안요청서'})
db.keywords.insert_one({'keyword' : '경쟁입찰'})
db.keywords.insert_one({'keyword' : '입찰PT'})
db.keywords.insert_one({'keyword' : '입찰경쟁'})
db.keywords.insert_one({'keyword' : '입찰제안'})
db.keywords.insert_one({'keyword' : '입찰제안서'})
db.keywords.insert_one({'keyword' : '조달청입찰'})
db.keywords.insert_one({'keyword' : 'RFP'})
db.keywords.insert_one({'keyword' : 'RFQ'})
db.keywords.insert_one({'keyword' : 'RFI'})
db.keywords.insert_one({'keyword' : '경쟁PT'})
db.keywords.insert_one({'keyword' : '경쟁프레젠테이션'})
db.keywords.insert_one({'keyword' : '제안서PPT'})
db.keywords.insert_one({'keyword' : '제안서PT'})
db.keywords.insert_one({'keyword' : '제안발표'})
db.keywords.insert_one({'keyword' : '입찰프레젠테이션'})
db.keywords.insert_one({'keyword' : '제안서컨설팅'})
db.keywords.insert_one({'keyword' : '기업교육컨설팅'})
db.keywords.insert_one({'keyword' : '기업컨설팅'})
db.keywords.insert_one({'keyword' : '수주컨설팅'})
db.keywords.insert_one({'keyword' : '입찰컨설팅'})
db.keywords.insert_one({'keyword' : '제안컨설팅'})
db.keywords.insert_one({'keyword' : 'B2B영업컨설팅'})
db.keywords.insert_one({'keyword' : '해외영업컨설팅'})
db.keywords.insert_one({'keyword' : '회사컨설팅'})
db.keywords.insert_one({'keyword' : 'PT컨설팅'})
db.keywords.insert_one({'keyword' : 'IR컨설팅'})
db.keywords.insert_one({'keyword' : '회사소개자료'})
db.keywords.insert_one({'keyword' : '회사소개서'})
db.keywords.insert_one({'keyword' : '교육컨설팅'})
db.keywords.insert_one({'keyword' : '수출바우처사업'})
db.keywords.insert_one({'keyword' : '수출바우처수행기관'})
db.keywords.insert_one({'keyword' : '수출역량강화'})
db.keywords.insert_one({'keyword' : '수출지원'})
db.keywords.insert_one({'keyword' : '바이어정보'})
db.keywords.insert_one({'keyword' : '바이어발굴'})
db.keywords.insert_one({'keyword' : '바우처사업'})
db.keywords.insert_one({'keyword' : '월드클래스300'})
db.keywords.insert_one({'keyword' : 'WC300'})
db.keywords.insert_one({'keyword' : '언택트세일즈'})
db.keywords.insert_one({'keyword' : '디지털세일즈'})
db.keywords.insert_one({'keyword' : '언택트환경'})
db.keywords.insert_one({'keyword' : '온라인세일즈'})
db.keywords.insert_one({'keyword' : '비대면영업'})
db.keywords.insert_one({'keyword' : '비대면교육'})

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요

keywords = list(db.keywards.find({}))
for keyword in keywords:
    frontUrl = "https://ad.search.naver.com/search.naver?where=ad&sm=svc_nrs&query="+keyword['keyword']
    tailUrl = "&referenceId=&pagingIndex="
    postNum = 1
    for i in range(15):
        newUrl = frontUrl+tailUrl+str(postNum)
        postNum = postNum+1
        data = requests.get(newUrl, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        keyword = soup.select('#content > div > ol > li')

        count = 1
        for div in keyword:
            title = div.select_one('div.inner > a').text
            if '쉬플리코리아' in title:
                print(count,i+1, newUrl)
            count += 1