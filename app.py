import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
dbKeyword = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = dbKeyword.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# MongoDB에 insert 하기

# db.keywards.insert_one({'keyword' : '기업교육'})
# db.keywards.insert_one({'keyword' : '영업교육'})


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