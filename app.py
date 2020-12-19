import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
dbKeyword = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = dbKeyword.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

app = Flask(__name__)
@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('index.html')

@app.route('/keyword', methods=['POST'])
def post_keywords():
    # 1. 클라이언트로부터 데이터를 받기
    name_receive = request.form['name_give']  # 클라이언트로부터 키워드를 받는 부분
    keywordInfo = {'keyword': name_receive}
    # 몽고DB에 입력
    db.keywords.insert_one(keywordInfo)
    return jsonify({'result': 'success'})

@app.route('/keyword', methods=['GET'])
def read_keywords():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # 아래 빈 칸('')을 채워보세요

    keywords = list(db.keywords.find({}))
    # keywords = [{'keyword':'기업교육'}]
    orders = []
    for keyword in keywords:
        frontUrl = "https://ad.search.naver.com/search.naver?where=ad&sm=svc_nrs&query="+keyword['keyword']
        tailUrl = "&referenceId=&pagingIndex="
        postNum = 1
        for i in range(15):
            newUrl = frontUrl+tailUrl+str(postNum)
            postNum = postNum+1
            data = requests.get(newUrl, headers=headers)
            soup = BeautifulSoup(data.text, 'html.parser')
            page = soup.select('#content > div > ol > li')

            count = 1
            for div in page:
                title = div.select_one('div.inner > a').text
                if '쉬플리코리아' in title:
                    print(keyword['keyword'], count, i+1, newUrl)
                    news = {
                        'keyword':keyword['keyword'],
                        'count':count,
                        'page':i+1,
                        'newUrl':newUrl
                    }
                    orders.append(news)
                count += 1

    return jsonify({'result': 'success', 'keywords': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# MongoDB에 insert 하기



